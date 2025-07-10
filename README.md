🎵 YouTube 歌單 .webm 下載器
YouTube Playlist .webm Downloader
一個開源的 YouTube 歌單下載工具，可將整個歌單快速轉為 .webm 格式，支援局域網 QR Code 分享。你可以使用已編譯好的 .exe 執行檔，或執行 Python 原始碼。
(exe以沒有提供)
請自行安裝python 3.10系列,並依照下方只是進行依賴安裝,如有不變敬請見諒。

An open-source YouTube playlist downloader that converts full playlists into .webm files. Supports LAN QR code sharing. Run with the precompiled .exe, or launch from Python source.
(exe is not provided)
Please install Python 3.10 series by yourself and follow the instructions below to install the dependencies. Please forgive me if there are any changes.

🌟 功能 Features
✅ 一鍵下載整個 YouTube 歌單為 .webm
One-click download of full YouTube playlists as .webm

✅ 自動命名、整理檔案與標籤
Auto naming and metadata tagging

✅ 內建 QR Code 分享，手機輕鬆下載
QR code for mobile downloads via LAN

✅ 附帶 .exe，無需安裝 Python
Precompiled .exe available – no Python required

✅ 完全開源，歡迎修改與部署
Fully open-source and customizable

📦 免安裝版本 Executable Version
你可以直接執行 yt_music_downloader.exe，不需安裝 Python 或任何依賴。

You can run yt_music_downloader.exe directly. No Python installation needed.

⚠️ 第一次啟動可能需要 2–5 秒，請耐心等待。
⚠️ First launch may take a few seconds. Please be patient.

🧩 原始碼版 Dependencies
若要從原始碼執行，請先安裝依賴與 ffmpeg：

1️⃣ 安裝 Python 套件
請執行本目錄中的 PowerShell 腳本：

powershell
複製
編輯
./install_modules.ps1
這將自動安裝：

flask

yt-dlp

qrcode

請使用 PowerShell 執行；如果無法執行，請檢查 PowerShell 執行權限（Set-ExecutionPolicy RemoteSigned）

2️⃣ 安裝 ffmpeg 音訊/影片轉換工具
yt-dlp 需要用 ffmpeg 來處理 .webm 檔案。

Windows 安裝方式：
前往 https://www.gyan.dev/ffmpeg/builds/

下載「release full build」並解壓縮

將 bin 資料夾加入系統環境變數 Path

No Mac/Linux Instructions
本專案僅針對 Windows 提供 .exe，不支援 macOS 或 Linux。

💻 執行原始碼版 Run from Source
bash
複製
編輯
python server.py
然後在瀏覽器開啟：

arduino
複製
編輯
http://localhost:3000
輸入 YouTube 歌單連結即可下載。

📱 手機下載 QR Code 分享
任務完成後，網頁會自動顯示 QR Code。你可使用手機掃描，在同一 Wi-Fi 網路下直接下載檔案。

When a task is completed, a QR code will be generated for downloading from your phone over the LAN.

🛠 自行打包（可選）Build Your Own Executable (optional)
若你想要產生自己的 .exe：

bash
複製
編輯
pip install nuitka
python -m nuitka server.py --standalone --onefile
這會產生一個獨立的可執行檔（位於 server.exe）。

📜 授權 License
本專案使用 MIT License，可自由使用、修改與散佈。

This project is licensed under the MIT License.

Made with ❤️ by Zyen
