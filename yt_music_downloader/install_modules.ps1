# Install virtual environment and dependencies
Write-Host "🔧 Creating virtual environment (.venv)..."

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "❌ Python not found. Please install Python 3.10 or newer before running this script."
    exit 1
}

python -m venv .venv

Write-Host "✅ Virtual environment created. Installing dependencies..."

& .\.venv\Scripts\pip install --upgrade pip
& .\.venv\Scripts\pip install flask yt-dlp qrcode

Write-Host "✅ All dependencies installed!"
Write-Host "👉 Use run_server.ps1 to start the server."
