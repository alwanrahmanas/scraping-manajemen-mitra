@echo off
echo ============================================
echo Installing OpenAI Dependencies
echo ============================================
echo.

echo Installing openai and python-dotenv...
pip install openai>=1.0.0 python-dotenv>=1.0.0

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Copy .env.example to .env
echo 2. Edit .env and add your OpenAI API key
echo 3. Run: python scrape_mitra_no_pandas.py
echo.
pause
