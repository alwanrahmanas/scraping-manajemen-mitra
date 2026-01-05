@echo off
echo ========================================
echo Starting Chrome with Remote Debugging
echo ========================================
echo.
echo Chrome akan terbuka dengan debugging port 9222
echo Silakan login ke website dan buka halaman Seleksi Mitra
echo.
echo PENTING: Jangan tutup window Chrome ini!
echo.

start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%TEMP%\chrome-debug-profile"

echo.
echo Chrome telah dibuka. Setelah login, jalankan: run.bat
echo.
pause
