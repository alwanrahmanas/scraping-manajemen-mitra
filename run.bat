@echo off
echo ========================================
echo Mitra BPS Scraper
echo ========================================
echo.

echo Memastikan Chrome dengan debugging sudah berjalan...
echo Jika belum, jalankan: start_chrome.bat
echo.

echo Memulai scraping...
echo Progress akan ditampilkan di console dan disimpan ke log file
echo.
python scrape_mitra.py

echo.
echo ========================================
echo Scraping selesai!
echo ========================================
echo.
echo Hasil tersimpan di:
echo - mitra_data.xlsx (Excel dengan formatting)
echo - mitra_data.csv (CSV backup)
echo - downloads/ (foto KTP dan Ijazah)
echo - scraper_*.log (log file detail)
echo.
echo Buka file Excel untuk melihat data dengan format yang rapi!
echo Buka file log untuk melihat detail proses scraping.
echo.
pause

