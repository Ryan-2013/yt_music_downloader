from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
import threading
import os
import yt_dlp
import qrcode
import io
import base64
import socket

app = Flask(__name__)

downloads = {}  # 儲存任務資訊 {task_id: {status, dir, ...}}

def get_local_ip():
    """取得本機局域網IP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def download_playlist(url, task_id, base_dir='downloads'):
    downloads[task_id] = {'status': '下載中', 'dir': None}

    try:
        os.makedirs(base_dir, exist_ok=True)
        info_opts = {'quiet': True, 'extract_flat': True, 'dump_single_json': True}
        with yt_dlp.YoutubeDL(info_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        playlist_title = info.get('title', 'Unknown_Playlist').strip().replace('/', '_').replace('\\', '_')
        playlist_dir = os.path.join(base_dir, playlist_title)
        os.makedirs(playlist_dir, exist_ok=True)

        ydl_opts = {
            'outtmpl': f'{playlist_dir}/%(playlist_index)03d - %(title).100s.%(ext)s',
            'format': 'bestaudio/best',
            'ignoreerrors': True,
            'noplaylist': False,
            'quiet': True,
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                },
                {
                    # 嵌入標題與封面資訊（若有）
                    'key': 'FFmpegMetadata',
                }
            ],
            # 針對不支援標題的系統避免出現非法字元
            'postprocessor_args': [
                '-metadata', 'encoding=UTF-8',
                '-id3v2_version', '3',
            ],
            'prefer_ffmpeg': True,
            'ffmpeg_location': 'ffmpeg',  # 確保 ffmpeg 在 PATH 中（可視環境調整）
            'unicode_bom': True,  # 強制 UTF-8 with BOM
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        downloads[task_id]['status'] = '下載完成'
        downloads[task_id]['dir'] = playlist_dir
        downloads[task_id]['title'] = playlist_title

    except Exception as e:
        downloads[task_id]['status'] = f'下載失敗: {e}'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template('index.html', error='請輸入歌單網址')
        # 產生任務ID (簡單用時間戳)
        import time
        task_id = str(int(time.time()*1000))
        downloads[task_id] = {'status': '尚未開始', 'dir': None}

        # 啟動下載執行緒
        threading.Thread(target=download_playlist, args=(url, task_id)).start()

        # 轉向狀態頁
        return render_template('status.html', task_id=task_id)
    return render_template('index.html')


@app.route('/status/<task_id>')
def status(task_id):
    task = downloads.get(task_id)
    if not task:
        return jsonify({'status': '無此下載任務'}), 404

    response = {'status': task['status']}

    if task['status'] == '下載完成' and task['dir']:
        files = []
        for f in os.listdir(task['dir']):
            if f.lower().endswith('.mp3'):
                url = url_for('serve_file', task_id=task_id, filename=f)
                files.append({'name': f, 'url': url})

        # 產生局域網 URL 及 QR Code
        local_ip = get_local_ip()
        port = request.host.split(':')[1] if ':' in request.host else '5000'
        lan_url = f"http://{local_ip}:{port}/status/{task_id}"

        qr = qrcode.QRCode(box_size=6, border=2)
        qr.add_data(lan_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        qr_code_b64 = base64.b64encode(buf.getvalue()).decode('ascii')

        response['files'] = files
        response['qr_code'] = qr_code_b64
        response['lan_url'] = lan_url

    return jsonify(response)

@app.route('/download/<task_id>/<filename>')
def serve_file(task_id, filename):
    task = downloads.get(task_id)
    if not task or not task['dir']:
        return "檔案不存在", 404
    return send_from_directory(task['dir'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
