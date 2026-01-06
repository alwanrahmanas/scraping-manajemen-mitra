# 🚀 Scraping Manajemen Mitra BPS

Automated web scraper untuk mengekstrak data mitra dari sistem Manajemen Mitra BPS, dengan fitur AI-powered parsing ijazah menggunakan OpenAI Vision API.

---

## ✨ Fitur Utama

- ✅ **Scraping Otomatis** - Extract data NIK, rekening bank, dan informasi mitra
- 🤖 **AI-Powered Ijazah Parser** - Parse ijazah otomatis dengan OpenAI Vision API
- 📊 **Excel & CSV Output** - Export data ke format Excel dan CSV
- 🗂️ **Versioning Otomatis** - Setiap run disimpan di folder dengan timestamp
- 🖼️ **Download Gambar** - Download KTP dan ijazah otomatis
- 🔍 **Identifikasi Jenis Ijazah** - Deteksi otomatis SMA/SMK vs Perguruan Tinggi
- 🧹 **Regex Cleaning** - Nomor rekening dibersihkan (hanya angka)

---

## 📋 Prerequisites

1. **Python 3.8+**
2. **Google Chrome** (sudah terinstall)
3. **OpenAI API Key** (untuk parsing ijazah)

---

## 🛠️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/alwanrahmanas/scraping-manajemen-mitra.git
cd scraping-manajemen-mitra
```

### 2. Install Dependencies

```bash
setup.bat
```

Atau manual:
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Setup OpenAI API Key

Buat file `.env` di root folder:

```env
OPENAI_API_KEY=your_api_key_here
```

Atau copy dari template:
```bash
copy .env.example .env
```
Lalu edit `.env` dan masukkan API key Anda.

---

## 🚀 Cara Menggunakan

### **Testing (3 Data Pertama)**

```bash
run_test.bat
```

Output akan tersimpan di: `output_test_YYYYMMDD_HHMMSS/`

### **Full Scraping (Semua Data)**

```bash
run.bat
```

Output akan tersimpan di: `output_YYYYMMDD_HHMMSS/`

---

## 📂 Struktur Output

```
output_20260106_150000/
├── mitra_data.xlsx          # Excel output
├── mitra_data.csv            # CSV backup
└── downloads/                # Folder gambar
    ├── 7410011110800001/
    │   ├── ktp.jpg
    │   └── ijazah.jpg
    ├── 7410036005020001/
    └── ...
```

---

## 📊 Kolom Output Excel

| Kolom | Deskripsi |
|-------|-----------|
| NIK | Nomor Induk Kependudukan |
| Nama Lengkap (dengan Gelar) | Dari parsing ijazah |
| Nomor Rekening | Dibersihkan (hanya angka) |
| Nama Bank | Nama bank |
| Nama Pemilik Rekening | Nama pemilik rekening |
| **Jenis Ijazah** | SMA/SMK atau Perguruan Tinggi |
| Gelar | Gelar akademik (S.Kom, S.E., dll) |
| NIM | Nomor Induk Mahasiswa |
| Program Studi | Program studi |
| Fakultas | Fakultas |
| Universitas | Nama universitas/sekolah |
| Tanggal Ijazah | Tanggal kelulusan |
| Path KTP | Path file KTP |
| Path Ijazah | Path file ijazah |
| Status | Success/Failed |

---

## 🔧 Utility Scripts

### **Re-parse Semua Ijazah**
```bash
python reparse_ijazah.py
```

### **Re-parse Ijazah Spesifik**
```bash
python reparse_single.py 7410036005020001
```

---

## 📖 Dokumentasi Lengkap

- **[SETUP_IJAZAH_PARSER.md](SETUP_IJAZAH_PARSER.md)** - Setup OpenAI API
- **[INTEGRASI_IJAZAH_PARSER.md](INTEGRASI_IJAZAH_PARSER.md)** - Integrasi parser
- **[FITUR_VERSIONING.md](FITUR_VERSIONING.md)** - Versioning output
- **[OUTPUT_EXCEL.md](OUTPUT_EXCEL.md)** - Struktur output Excel
- **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - Panduan testing

---

## ⚙️ Konfigurasi

### **Chrome Remote Debugging**

Script memerlukan Chrome yang berjalan dengan remote debugging:

```bash
start_chrome.bat
```

Atau manual:
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

### **Limit Testing**

Edit `scrape_mitra_test.py` line terakhir:
```python
scraper = MitraScraperTest(max_rows=3)  # Ubah angka sesuai kebutuhan
```

---

## 🐛 Troubleshooting

### **Error: "No suitable tab found"**
- Pastikan Chrome sudah dibuka dengan remote debugging
- Buka halaman "Seleksi Mitra" di Chrome
- Tutup tab DevTools atau foto jika ada

### **Error: "OPENAI_API_KEY not found"**
- Pastikan file `.env` sudah dibuat
- Pastikan API key sudah diisi dengan benar

### **Parsing Ijazah Gagal**
- Cek apakah foto ijazah jelas
- Coba re-parse dengan `reparse_single.py`
- Pertimbangkan upgrade ke model `gpt-4o` (lebih akurat tapi lebih mahal)

---

## 💰 Biaya OpenAI API

Estimasi biaya per ijazah: **~$0.01 - $0.02**

Model yang digunakan: `gpt-4o-mini`

Untuk akurasi lebih tinggi, bisa upgrade ke `gpt-4o` (edit `ijazah_parser.py`)

---

## 📝 Changelog

### v2.0.0 (2026-01-06)
- ✨ Tambah fitur versioning output dengan timestamp
- ✨ Tambah identifikasi jenis ijazah (SMA/SMK vs Perguruan Tinggi)
- ✨ Tambah regex cleaning untuk nomor rekening
- 🐛 Fix download KTP & Ijazah yang tertukar
- 🐛 Fix tab selection (skip DevTools & fs-storage)
- 🔧 Improve error handling & timeout handling
- 🔧 Better selector strategies untuk tab navigation

### v1.0.0 (2026-01-05)
- 🎉 Initial release
- ✨ Basic scraping functionality
- ✨ OpenAI Vision API integration
- ✨ Excel & CSV export

---

## 👨‍💻 Author

**Alwan Rahmana S**
- GitHub: [@alwanrahmanas](https://github.com/alwanrahmanas)

---

## 📄 License

This project is for internal use only.

---

## 🙏 Acknowledgments

- OpenAI for Vision API
- Playwright for browser automation
- BPS for the data source

---

## 📞 Support

Jika ada pertanyaan atau issue, silakan buat issue di GitHub repository.

---

**Happy Scraping! 🚀**
