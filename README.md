# 🎵 YouTube 歌單 .webm 下載器  
## YouTube Playlist .webm Downloader

一個開源的 YouTube 歌單下載工具，可將整個歌單快速轉為 .webm，支援局域網 QR Code 分享。你可以使用已編譯好的 `.exe` 執行檔，或直接執行 Python 原始碼。

An open-source YouTube playlist downloader that converts entire playlists into .webm files. Supports LAN QR code sharing. Run with the precompiled `.exe`, or launch via Python source.

---

## 🌟 功能 Features

- ✅ 一鍵下載整個 YouTube 歌單成 M.webm 
  One-click download of full YouTube playlists as MP3  
- ✅ 自動命名與 .webm 標籤整理  
  Auto naming and tagging of downloaded MP3s  
- ✅ QR Code 分享，可手機直接下載  
  QR code for easy mobile downloads over LAN  
- ✅ 附帶 `.exe` 可執行檔，免安裝 Python  
  Precompiled `.exe` included – no Python required  
- ✅ 完全開源，方便自訂與部署  
  Fully open-source and customizable  

---

## 📦 免安裝版本 Executable Version

你可以直接執行 `yt_music_downloader.exe`，不需要安裝 Python 或其他依賴。

You can run `yt_music_downloader.exe` directly. No Python setup required.

> ⚠️ 第一次執行可能需等待 2–5 秒，請耐心等候視窗開啟。  
> First launch may take a few seconds. Please be patient.

---

## 🧩 原始碼版 Dependencies

若要從原始碼執行，需安裝以下依賴：

### 1️⃣ 安裝 Python 套件（需 Python 3.10+）

```bash
pip install flask yt-dlp qrcode



```
### 2️⃣ 安裝 ffmpeg
這是音訊轉檔工具，yt-dlp 會用它來產出 mp3。

Windows：
到 https://www.gyan.dev/ffmpeg/builds/

下載「release full build」並解壓縮

將 bin 資料夾加入系統環境變數 Path

Download "release full build" and unzip it

Add the bin folder to the system environment variable Path

沒有介紹mac和linux板式因為只有提供exe檔
There is no introduction to Mac and Linux versions because only exe files are provided

💻 執行原始碼版 Run from Source
bash
複製
編輯
python server.py
然後在瀏覽器輸入網址：

arduino
複製
編輯
http://localhost:3000
輸入 YouTube 歌單連結，即可下載。

📱 手機下載 QR Code 分享
當任務完成後，網頁會自動產生 QR Code。你可以使用手機掃描，在同一個 Wi-Fi 下直接下載歌曲。

The app generates a QR code for each completed task. You can scan it with your phone and download MP3 files over LAN.

🛠 打包方式（可選）Build Your Own Executable (optional)
若你想自行打包：

bash
複製
編輯
pip install nuitka
python -m nuitka server.py --standalone --onefile
會產生一個獨立的 .exe 檔案，可在 Windows 上執行。

📜 授權 License
本專案使用 MIT License，你可以自由使用、修改與發佈。

This project is licensed under the MIT License.


Made with ❤️ by Zyen.


