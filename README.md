# 🎵 YouTube 歌單 MP3 下載器  
## YouTube Playlist MP3 Downloader

一個開源的 YouTube 歌單下載工具，可將整個歌單快速轉為 MP3，支援局域網 QR Code 分享。你可以使用已編譯好的 `.exe` 直接執行，或執行 Python 原始碼。

An open-source YouTube playlist downloader that converts entire playlists into MP3 files. LAN QR code sharing supported. You can either run the precompiled `.exe`, or launch from Python source.

---

## 🌟 功能 Features

- ✅ 一鍵下載整個 YouTube 歌單成 MP3  
  One-click download of full YouTube playlists as MP3  
- ✅ 自動命名與標籤整齊分類  
  Auto naming and tagging of downloaded songs  
- ✅ 透過 QR Code 分享給手機下載  
  QR Code for mobile access in local network  
- ✅ 提供 `.exe` 可執行檔，無需安裝 Python  
  Comes with precompiled `.exe`, no Python needed  
- ✅ 完全開源，可自訂與自行部署  
  Fully open-source and customizable  

---

## 📦 免安裝版本 Executable Version

你可以直接執行 `yt_music_downloader.exe`，不需要安裝 Python 或任何額外工具。

You can run `yt_music_downloader.exe` directly. No Python or setup required.

> ⚠️ 注意：第一次執行可能會稍微等待 2–5 秒，請耐心等待視窗開啟。

---

## 🧩 依賴項 Dependencies

如果你想執行原始碼版本，需要安裝以下依賴：

### 1️⃣ 安裝 Python 套件（Python 3.10+）

```bash
pip install flask yt-dlp qrcode



2️⃣ 安裝 ffmpeg
這是音訊轉檔工具，yt-dlp 會用它來產出 mp3。

Windows：
到 https://www.gyan.dev/ffmpeg/builds/

下載「release full build」並解壓縮

將 bin 資料夾加入系統環境變數 Path

macOS：
bash
複製
編輯
brew install ffmpeg
Linux：
bash
複製
編輯
sudo apt install ffmpeg
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


