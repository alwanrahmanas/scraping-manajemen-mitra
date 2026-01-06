@echo off
echo ========================================
echo PUSH TO GITHUB
echo ========================================
echo.

echo [1/5] Menambahkan semua file...
git add -A
echo   ✓ Files added

echo.
echo [2/5] Membuat commit...
git commit -m "feat: Major update - AI parsing, versioning, improved selectors"
echo   ✓ Commit created

echo.
echo [3/5] Checking remote...
git remote -v
echo.

echo [4/5] Force push ke GitHub (akan menimpa semua file)...
echo PERINGATAN: Ini akan menimpa seluruh repository di GitHub!
echo.
pause

git push -f origin main
echo   ✓ Pushed to GitHub

echo.
echo ========================================
echo ✓ PUSH SELESAI!
echo ========================================
echo.
echo Repository: https://github.com/alwanrahmanas/scraping-manajemen-mitra
echo.
pause
