@echo off
echo ========================================
echo PUSH TO GITHUB - FIXED
echo ========================================
echo.

echo [1/6] Checking current branch...
git branch
echo.

echo [2/6] Checking if main branch exists...
git show-ref --verify --quiet refs/heads/main
if %errorlevel% neq 0 (
    echo Branch 'main' tidak ada, membuat branch baru...
    git checkout -b main
    echo   ✓ Branch main created
) else (
    echo Branch 'main' sudah ada
    git checkout main
)
echo.

echo [3/6] Menambahkan semua file...
git add -A
echo   ✓ Files added
echo.

echo [4/6] Membuat commit...
git commit -m "feat: Major update - AI parsing, versioning, improved selectors"
if %errorlevel% neq 0 (
    echo   ⚠ No changes to commit or commit failed
) else (
    echo   ✓ Commit created
)
echo.

echo [5/6] Setting remote (jika belum ada)...
git remote remove origin 2>nul
git remote add origin https://github.com/alwanrahmanas/scraping-manajemen-mitra.git
echo   ✓ Remote set
echo.

echo [6/6] Force push ke GitHub...
echo PERINGATAN: Ini akan menimpa seluruh repository di GitHub!
echo.
pause

git push -f origin main
if %errorlevel% neq 0 (
    echo.
    echo   ✗ Push failed!
    echo.
    echo Possible solutions:
    echo 1. Check your internet connection
    echo 2. Check if you have access to the repository
    echo 3. Try: git push -f -u origin main
    echo.
) else (
    echo   ✓ Pushed to GitHub
)

echo.
echo ========================================
echo PUSH PROCESS COMPLETED
echo ========================================
echo.
echo Repository: https://github.com/alwanrahmanas/scraping-manajemen-mitra
echo.
pause
