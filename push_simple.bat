@echo off
echo ========================================
echo PUSH TO GITHUB - SIMPLE VERSION
echo ========================================
echo.

REM Initialize git if needed
if not exist .git (
    echo Initializing git repository...
    git init
    echo   ✓ Git initialized
)
echo.

REM Create main branch and switch to it
echo Creating/switching to main branch...
git checkout -B main
echo   ✓ On main branch
echo.

REM Add all files
echo Adding all files...
git add -A
echo   ✓ Files added
echo.

REM Commit
echo Creating commit...
git commit -m "feat: Major update - AI parsing, versioning, improved selectors" -m "- Add AI-powered ijazah parsing with OpenAI Vision API" -m "- Add automatic versioning with timestamp folders" -m "- Add jenis ijazah detection (SMA/SMK vs Perguruan Tinggi)" -m "- Add regex cleaning for nomor rekening" -m "- Fix KTP & Ijazah download selectors" -m "- Fix tab selection (skip DevTools & fs-storage)" -m "- Improve error handling & timeout handling"
echo   ✓ Commit created
echo.

REM Set remote
echo Setting remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/alwanrahmanas/scraping-manajemen-mitra.git
echo   ✓ Remote set
echo.

REM Push
echo.
echo ========================================
echo READY TO PUSH!
echo ========================================
echo.
echo This will OVERWRITE the entire repository on GitHub!
echo Repository: https://github.com/alwanrahmanas/scraping-manajemen-mitra
echo.
pause

echo.
echo Pushing to GitHub...
git push -f origin master

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo ✓ SUCCESS!
    echo ========================================
    echo.
    echo Repository updated: https://github.com/alwanrahmanas/scraping-manajemen-mitra
) else (
    echo.
    echo ========================================
    echo ✗ PUSH FAILED
    echo ========================================
    echo.
    echo Troubleshooting:
    echo 1. Check internet connection
    echo 2. Verify GitHub access
    echo 3. Try manual push: git push -f origin master
)

echo.
pause
