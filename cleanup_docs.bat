@echo off
echo ========================================
echo CLEANUP DOKUMENTASI
echo ========================================
echo.

echo Menghapus file dokumentasi yang tidak relevan...
echo.

REM Hapus dokumentasi lama
if exist TESTING_GUIDE.md (
    del /f TESTING_GUIDE.md
    echo   ✓ TESTING_GUIDE.md dihapus
)

if exist OUTPUT_EXCEL.md (
    del /f OUTPUT_EXCEL.md
    echo   ✓ OUTPUT_EXCEL.md dihapus
)

if exist FITUR_VERSIONING.md (
    del /f FITUR_VERSIONING.md
    echo   ✓ FITUR_VERSIONING.md dihapus
)

if exist INTEGRASI_IJAZAH_PARSER.md (
    del /f INTEGRASI_IJAZAH_PARSER.md
    echo   ✓ INTEGRASI_IJAZAH_PARSER.md dihapus
)

if exist SETUP_IJAZAH_PARSER.md (
    del /f SETUP_IJAZAH_PARSER.md
    echo   ✓ SETUP_IJAZAH_PARSER.md dihapus
)

if exist FIX_PUSH_ERROR.md (
    del /f FIX_PUSH_ERROR.md
    echo   ✓ FIX_PUSH_ERROR.md dihapus
)

if exist PUSH_CHECKLIST.md (
    del /f PUSH_CHECKLIST.md
    echo   ✓ PUSH_CHECKLIST.md dihapus
)

echo.
echo ========================================
echo ✓ CLEANUP SELESAI!
echo ========================================
echo.
echo Dokumentasi yang tersisa:
echo - README.md (Panduan utama)
echo - SETUP_API_KEY.md (Cara setup OpenAI)
echo.
pause
