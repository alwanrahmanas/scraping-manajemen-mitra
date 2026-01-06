@echo off
echo ============================================
echo Running Mitra BPS Scraper
echo ============================================
echo.

echo IMPORTANT:
echo 1. Make sure Chrome is running (start_chrome.bat)
echo 2. Make sure you are logged in to the website
echo 3. Make sure you are on the "Seleksi Mitra" page
echo.

set /p confirm="Ready to start scraping? (Y/N): "
if /i "%confirm%" NEQ "Y" (
    echo Scraping cancelled.
    pause
    exit /b
)

echo.
echo Starting scraper...
echo.

python scrape_mitra.py

echo.
echo ============================================
echo Scraping finished!
echo ============================================
echo.
echo Check the output files:
echo - mitra_data.xlsx (Excel with formatting)
echo - mitra_data.csv (CSV backup)
echo - downloads\ folder (KTP and Ijazah images)
echo - scraper_*.log (detailed log file)
echo.
pause
