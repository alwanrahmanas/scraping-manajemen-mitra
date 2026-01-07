@echo off
echo ============================================================
echo GIT PUSH: MISMATCH DETECTION & HIGHLIGHTING FEATURES
echo ============================================================

echo Checking status...
git status

echo.
echo Adding files...
git add scrape_mitra.py
git add MISMATCH_DETECTION.md
git add test_mismatch_highlighting.py
git add ijazah_parser.py
git add reparse_ijazah.py
:: Add other files if needed, but these are the main ones modified/created today
git add .

echo.
echo Committing changes...
git commit -m "feat: add mismatch detection and auto-highlighting in Excel"

echo.
echo Pushing to repository...
git push

echo.
echo ============================================================
echo DONE! Changes pushed successfully.
echo ============================================================
pause
