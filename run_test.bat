@echo off
echo ============================================
echo Running Mitra BPS Scraper - TESTING MODE
echo ============================================
echo.
echo This will scrape ONLY 5 people for testing
echo.

echo IMPORTANT:
echo 1. Make sure Chrome is running (start_chrome.bat)
echo 2. Make sure you are logged in to the website
echo 3. Make sure you are on the "Seleksi Mitra" page
echo.

set /p confirm="Ready to start testing? (Y/N): "
if /i "%confirm%" NEQ "Y" (
    echo Testing cancelled.
    pause
    exit /b
)

echo.
echo Starting test scraper (5 people only)...
echo.

python scrape_mitra_test.py

echo.
echo ============================================
echo Testing finished!
echo ============================================
echo.
echo Check the output files:
echo - mitra_data_test.xlsx (Excel with 10 people)
echo - mitra_data_test.csv (CSV backup)
echo - downloads_test\ folder (KTP and Ijazah images)
echo - scraper_test_*.log (detailed log file)
echo.
echo If testing is successful, run the full scraper with:
echo   run.bat
echo.
pause
