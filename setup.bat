@echo off
echo ============================================
echo SETUP - Mitra BPS Scraper
echo ============================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Installing Playwright browsers...
playwright install chromium

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Setup OpenAI API (optional, for ijazah parsing):
echo    - Run: install_openai.bat (already done if requirements.txt installed)
echo    - Edit .env and add your OpenAI API key
echo.
echo 2. Start Chrome with debugging:
echo    - Run: start_chrome.bat
echo.
echo 3. Run the scraper:
echo    - Run: run.bat
echo.
pause
