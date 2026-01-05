@echo off
echo ========================================
echo Setup Mitra BPS Scraper
echo ========================================
echo.

echo [1/2] Installing Python dependencies...
pip install -r requirements.txt

echo.
echo [2/2] Installing Playwright browsers...
python -m playwright install chromium

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Run Chrome with debugging: start_chrome.bat
echo 2. Login to the website
echo 3. Run the scraper: run.bat
echo.
pause
