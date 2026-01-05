# Mitra BPS Scraper

Script untuk scraping data mitra dari halaman Seleksi Mitra BPS dengan **logging detail** dan **export ke Excel**.

## ✨ Fitur

- ✅ **Scraping data rekening** (Nama Bank, Nomor Rekening, Nama Pemilik)
- ✅ **Download foto KTP dan Ijazah** otomatis
- ✅ **Export ke Excel** dengan formatting profesional
- ✅ **Logging detail** ke file dan console
- ✅ **Progress tracking** real-time
- ✅ **Pagination otomatis** - proses semua halaman
- ✅ **Error handling** dan recovery otomatis
- ✅ **Statistik lengkap** setelah scraping selesai

## 📋 Cara Penggunaan

### 1. Setup (Pertama Kali)

```cmd
setup.bat
```

Tunggu sampai selesai. Script akan install:
- playwright
- requests  
- openpyxl

### 2. Jalankan Chrome dengan Debugging

```cmd
start_chrome.bat
```

Chrome akan terbuka. **Login** ke website dan buka halaman **Seleksi Mitra**.

⚠️ **PENTING**: Jangan tutup window Chrome ini selama scraping!

### 3. Jalankan Scraper

```cmd
run.bat
```

Script akan otomatis:
- Membaca semua baris di tabel (skip header rows)
- Klik setiap NIK untuk membuka detail
- Klik tab "File Administrasi" → Download KTP & Ijazah
- Klik tab "Rekening" → Scrape data bank
- Simpan ke Excel dengan formatting
- **Otomatis lanjut ke halaman berikutnya** (pagination)
- Generate log file detail

## 📊 Output

### 1. File Excel: `mitra_data.xlsx`

Excel dengan formatting profesional:
- **Header berwarna biru** dengan teks putih bold
- **Auto-width columns** untuk readability
- **Borders** pada semua cell
- **Sheet name**: "Data Mitra"

| NIK | Nama Bank | Nomor Rekening | Nama Pemilik | Path KTP | Path Ijazah | Status |
|-----|-----------|----------------|--------------|----------|-------------|--------|
| 7410011110800001 | (002) BANK BRI | 707601025054539 | ASMAN | downloads/... | downloads/... | Success |

### 2. Folder Downloads: `downloads/`

```
downloads/
├── 7410011110800001/
│   ├── ktp.jpg
│   └── ijazah.jpg
├── 7410030107670045/
│   ├── ktp.jpg
│   └── ijazah.jpg
└── ...
```

### 3. Log File: `scraper_YYYYMMDD_HHMMSS.log`

Log detail dengan informasi:
- ✅ Timestamp setiap aksi
- 📊 Progress per row dan per page
- 🔍 Detail ekstraksi data
- 📷 Status download gambar (dengan ukuran file)
- ⚠️ Error messages dengan stack trace
- 📈 Summary statistik

**Contoh Log:**
```
============================================================
MITRA BPS SCRAPER - STARTING
============================================================
✓ Connected to: Seleksi Mitra : Manajemen Mitra
✓ Found 10 data rows (skipped 2 header rows)
✓ Detected total pages: 19

============================================================
PROCESSING PAGE 1
============================================================

============================================================
Processing Row 1: NIK 7410011110800001
============================================================
✓ Popup opened

--- Processing File Administrasi ---
✓ Clicked File Administrasi tab
Found 2 images in modal
✓ Downloaded ktp.jpg (245.67 KB) -> downloads/7410011110800001/ktp.jpg
✓ Downloaded ijazah.jpg (312.45 KB) -> downloads/7410011110800001/ijazah.jpg

--- Processing Rekening ---
✓ Clicked Rekening tab
Found Nama Bank: (002) BANK BRI
Found Nomor Rekening: 707601025054539
Found Nama Pemilik: ASMAN

✓ Successfully processed NIK 7410011110800001
  Bank: (002) BANK BRI
  Rekening: 707601025054539
  Pemilik: ASMAN

... (rows 2-10) ...

✓ Page 1 completed. Moving to next page...
✓ Found 10 rows on page 2

============================================================
PROCESSING PAGE 2
============================================================
... (lanjut sampai page 19) ...

============================================================
SCRAPING SUMMARY
============================================================
Pages processed: 19
Total rows processed: 190
✓ Successful: 185
✗ Failed: 5
📷 KTP downloaded: 180
📷 Ijazah downloaded: 178
============================================================
```

## ⏱️ Estimasi Waktu

- **Per row**: ~8-12 detik
- **Per page** (10 rows): ~2 menit  
- **Total** (19 pages × 10 rows): **~30-40 menit**

## 🔧 Troubleshooting

### Error: "Could not connect to browser"

- Pastikan Chrome sudah dijalankan dengan `start_chrome.bat`
- Pastikan tidak ada Chrome lain yang sedang berjalan
- Check log file untuk detail error

### Error: Selector tidak ditemukan

- Pastikan sudah login ke website
- Pastikan sudah berada di halaman Seleksi Mitra
- Tunggu halaman selesai loading sebelum menjalankan scraper
- Periksa log file untuk melihat di mana error terjadi

### Download gambar gagal

- Periksa koneksi internet
- Periksa apakah URL gambar valid (lihat di log)
- Beberapa gambar mungkin memerlukan autentikasi khusus
- Log akan menunjukkan HTTP status code jika gagal

### Data tidak lengkap

- Periksa log file untuk melihat fallback parsing
- Struktur HTML mungkin berbeda dari yang diharapkan
- Script akan tetap menyimpan data yang berhasil diambil

## 📝 Catatan

- Script menggunakan **Playwright** untuk kontrol browser
- Menggunakan **Chrome DevTools Protocol (CDP)** untuk connect ke browser yang sudah login
- **Logging** ke file dan console secara bersamaan
- **Excel** dengan openpyxl untuk formatting profesional
- **CSV backup** juga disimpan untuk kompatibilitas
- **Error recovery** otomatis untuk melanjutkan scraping meski ada error
- **Pagination otomatis** - tidak perlu manual klik "Selanjutnya"

## 🎯 Tips

1. **Monitor Progress**: Lihat console untuk progress real-time
2. **Check Log**: Buka file log untuk detail lengkap
3. **Jangan Minimize**: Biarkan Chrome window visible agar tidak ada masalah visibility
4. **Excel Tips**: Buka file Excel untuk analisis data dengan filter dan pivot table
5. **Batch Processing**: Script otomatis proses semua halaman tanpa intervensi manual

## 📂 File Structure

```
scraping-manajemen-mitra/
├── scrape_mitra.py          # Script utama
├── requirements.txt         # Dependencies
├── setup.bat                # Setup installer
├── start_chrome.bat         # Start Chrome dengan debugging
├── run.bat                  # Run scraper
├── README.md                # Dokumentasi ini
├── .gitignore               # Git ignore rules
├── downloads/               # Output folder (generated)
├── mitra_data.xlsx          # Output Excel (generated)
├── mitra_data.csv           # Output CSV (generated)
└── scraper_*.log            # Log files (generated)
```
