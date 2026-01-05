@echo off
echo ========================================
echo Setup Mitra BPS Scraper (Minimal)
echo ========================================
echo.

echo [1/2] Installing minimal dependencies...
echo (playwright, requests, openpyxl only - no pandas)
echo.
pip install -r requirements_minimal.txt

echo.
echo [2/2] Installing Playwright browsers...
python -m playwright install chromium

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Script yang akan digunakan: scrape_mitra_no_pandas.py
echo.
echo Next steps:
echo 1. Run Chrome with debugging: start_chrome.bat
echo 2. Login to the website
echo 3. Run the scraper: run_minimal.bat
echo.
pause
