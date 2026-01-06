@echo off
echo ========================================
echo CLEANUP - Hapus File Tidak Berguna
echo ========================================
echo.

REM Hapus file Python yang tidak digunakan
echo [1/5] Menghapus file Python lama...
if exist ijazah_parser_improved.py del /f ijazah_parser_improved.py
if exist ijazah_parser_old.py del /f ijazah_parser_old.py
echo   ✓ File Python lama dihapus

REM Hapus output lama (bukan folder versioning)
echo [2/5] Menghapus output lama...
if exist mitra_data.csv del /f mitra_data.csv
if exist mitra_data.xlsx del /f mitra_data.xlsx
if exist mitra_data_test.csv del /f mitra_data_test.csv
if exist mitra_data_test.xlsx del /f mitra_data_test.xlsx
echo   ✓ Output lama dihapus

REM Hapus folder downloads lama
echo [3/5] Menghapus folder downloads lama...
if exist downloads rmdir /s /q downloads
if exist downloads_test rmdir /s /q downloads_test
echo   ✓ Folder downloads lama dihapus

REM Hapus log files
echo [4/5] Menghapus log files...
del /f /q *.log 2>nul
echo   ✓ Log files dihapus

REM Hapus dokumentasi lama yang sudah tidak relevan
echo [5/5] Menghapus dokumentasi lama...
if exist BUGFIX_CSV_EXPORT.md del /f BUGFIX_CSV_EXPORT.md
if exist CLEANUP_ANALYSIS.md del /f CLEANUP_ANALYSIS.md
if exist LAPORAN_CLEANUP.md del /f LAPORAN_CLEANUP.md
if exist PERBAIKAN_DOWNLOAD_KTP_IJAZAH.md del /f PERBAIKAN_DOWNLOAD_KTP_IJAZAH.md
if exist PERBAIKAN_PARSING_IJAZAH.md del /f PERBAIKAN_PARSING_IJAZAH.md
if exist RINGKASAN_FINAL.md del /f RINGKASAN_FINAL.md
if exist SOLUSI_IJAZAH_BLUR.md del /f SOLUSI_IJAZAH_BLUR.md
if exist cleanup.bat del /f cleanup.bat
echo   ✓ Dokumentasi lama dihapus

echo.
echo ========================================
echo ✓ CLEANUP SELESAI!
echo ========================================
echo.
echo File yang tersisa:
echo - Script utama (scrape_mitra.py, scrape_mitra_test.py)
echo - Utility (ijazah_parser.py, reparse_*.py)
echo - Dokumentasi (README.md, *.md)
echo - Config (.env, requirements.txt)
echo - Batch files (run.bat, run_test.bat, setup.bat)
echo.
pause
