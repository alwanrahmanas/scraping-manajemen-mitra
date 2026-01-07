# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-01-07

### Added
- **Mismatch Detection**: Automatically detects if scraped account numbers contain non-numeric characters (indicating data mismatch).
- **Auto-Highlighting in Excel**: Rows with potential mismatches are now highlighted in red/pink in the output Excel file.
- **Summary Sheet**: Added a new "Summary" tab in the Excel output that shows data quality statistics and a legend for the highlighting.
- **Documentation**: Added `MISMATCH_DETECTION.md` detailing how the new detection system works.

### Changed
- **Scraping Timing**: Improved wait strategy for the "Rekening" tab to prevent race conditions where data from the previous row might be scraped.
- **Modal Handling**: Added explicit verification to ensure the detail modal is closed before proceeding to the next row, preventing data cross-contamination.
- **Logging**: Enhanced logging to provide real-time warnings when potential mismatches are detected.

## [2.0.0] - 2026-01-06

### Added
- **AI-Powered Parsing**: Integrated OpenAI Vision API to automatically read and extract data from diploma (ijazah) images.
- **Auto-Versioning**: Output folders are now timestamped to prevent overwriting previous runs.
- **Degree Detection**: Automatic detection of high school (SMA/SMK) vs University diplomas.
- **Regex Cleaning**: Automatic cleaning of account numbers to remove non-numeric characters.

### Fixed
- **Download Reliability**: Fixed issues where KTP and Ijazah images were failing to download.
- **Tab Selection**: Improved selectors for clicking through "File Administrasi" and "Rekening" tabs.

### Documentation
- Completely rewrote README.md for better clarity and ease of use.

## [1.0.0] - 2026-01-05

### Initial Release
- Basic scraping functionality for Mitra BPS website.
- Excel and CSV export.
- Automated browser navigation using Playwright.
