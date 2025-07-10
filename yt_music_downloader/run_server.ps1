# 確保虛擬環境存在
if (-not (Test-Path ".venv")) {
    Write-Host "The virtual environment has not been established yet, execute install_modules.ps1 first"
    exit 1
}

Write-Host "Starting Server..."
.venv\Scripts\activate
python server.py
