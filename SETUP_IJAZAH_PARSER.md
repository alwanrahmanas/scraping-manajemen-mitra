# Setup OpenAI API untuk Parsing Ijazah

## Langkah-langkah Setup

### 1. Install Dependencies Baru

Jalankan salah satu perintah berikut untuk menginstall dependencies yang diperlukan:

**Menggunakan setup.bat (dengan pandas):**
```bash
setup.bat
```

**Menggunakan setup_minimal.bat (tanpa pandas):**
```bash
setup_minimal.bat
```

Atau install manual:
```bash
pip install openai>=1.0.0 python-dotenv>=1.0.0
```

### 2. Konfigurasi API Key

1. **Copy file template `.env.example` menjadi `.env`:**
   ```bash
   copy .env.example .env
   ```

2. **Edit file `.env` dan masukkan OpenAI API key Anda:**
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

   > **PENTING:** Jangan pernah commit file `.env` ke Git! File ini sudah otomatis diabaikan oleh `.gitignore`.

### 3. Dapatkan OpenAI API Key

Jika Anda belum memiliki API key:

1. Kunjungi [OpenAI Platform](https://platform.openai.com/)
2. Login atau daftar akun
3. Buka [API Keys](https://platform.openai.com/api-keys)
4. Klik "Create new secret key"
5. Copy API key dan simpan di file `.env`

### 4. Cara Menggunakan

#### A. Scraping Otomatis dengan Parsing Ijazah

Setelah setup API key, script `scrape_mitra_no_pandas.py` akan **otomatis** melakukan parsing ijazah:

```bash
python scrape_mitra_no_pandas.py
```

**Fitur yang akan berjalan:**
- ✅ Download KTP dan Ijazah
- ✅ Parse ijazah dengan OpenAI Vision API
- ✅ Ekstrak informasi: nama, gelar, NIM, program studi, fakultas, universitas, tanggal ijazah
- ✅ Simpan hasil ke Excel dan CSV dengan kolom tambahan

**Jika API key tidak tersedia:**
- Script tetap berjalan normal
- KTP dan Ijazah tetap didownload
- Parsing ijazah di-skip
- Kolom ijazah akan berisi "N/A"

#### B. Testing Parser Ijazah Standalone

Untuk testing parser ijazah secara terpisah:

```bash
python ijazah_parser.py
```

Script ini akan:
- Mencari semua file `ijazah.jpg/jpeg/png` di folder `downloads/`
- Parse semua ijazah yang ditemukan
- Tampilkan hasil parsing di console

### 5. Output Excel

File Excel hasil scraping akan memiliki kolom-kolom berikut:

| Kolom | Deskripsi |
|-------|-----------|
| NIK | Nomor Induk Kependudukan |
| Nama Bank | Nama bank dari rekening |
| Nomor Rekening | Nomor rekening bank |
| Nama Pemilik | Nama pemilik rekening |
| Path KTP | Path file KTP yang didownload |
| Path Ijazah | Path file ijazah yang didownload |
| **Ijazah_Nama** | Nama lengkap dari ijazah (hasil parsing) |
| **Ijazah_Gelar** | Gelar akademik (S.Kom, S.T., dll) |
| **Ijazah_Nama_Gelar** | Kombinasi nama + gelar |
| **Ijazah_NIM** | Nomor Induk Mahasiswa |
| **Ijazah_Program_Studi** | Program studi |
| **Ijazah_Fakultas** | Fakultas |
| **Ijazah_Universitas** | Nama universitas |
| **Ijazah_Tanggal** | Tanggal penerbitan ijazah |
| Status | Status processing (Success/Failed) |

### 6. Biaya OpenAI API

Model yang digunakan: **gpt-4o-mini**

Estimasi biaya per ijazah:
- Input: ~$0.00015 per image (150 tokens @ $0.150/1M tokens)
- Output: ~$0.00006 per response (100 tokens @ $0.600/1M tokens)
- **Total: ~$0.0002 per ijazah** (sangat murah!)

Untuk 100 ijazah: ~$0.02 (sekitar Rp 300)

### 7. Troubleshooting

#### Error: "OpenAI API key tidak ditemukan"
- Pastikan file `.env` ada di root folder project
- Pastikan isi `.env` benar: `OPENAI_API_KEY=sk-proj-...`
- Jangan ada spasi sebelum/sesudah `=`

#### Error: "Invalid API key"
- Pastikan API key yang dimasukkan benar
- Cek apakah API key masih aktif di OpenAI dashboard
- Pastikan ada saldo/credit di akun OpenAI

#### Parsing gagal tapi download berhasil
- Cek log file untuk detail error
- Pastikan foto ijazah cukup jelas dan terbaca
- Script akan tetap menyimpan data dengan kolom ijazah = "N/A"

#### Ingin skip parsing ijazah
- Hapus atau rename file `.env`
- Script akan otomatis skip parsing dan hanya download

### 8. File Penting

```
scraping-manajemen-mitra/
├── .env                    # API key (JANGAN COMMIT!)
├── .env.example            # Template untuk .env
├── .gitignore              # Sudah include .env
├── ijazah_parser.py        # Modul parsing ijazah
├── scrape_mitra_no_pandas.py  # Script utama (sudah terintegrasi)
├── requirements.txt        # Dependencies (sudah include openai)
└── requirements_minimal.txt   # Dependencies minimal (sudah include openai)
```

### 9. Keamanan

✅ **File `.env` sudah otomatis diabaikan oleh Git**
- Tidak akan ter-commit ke repository
- API key Anda aman

⚠️ **Jangan pernah:**
- Commit file `.env` ke Git
- Share API key di public
- Hardcode API key di source code

### 10. Contoh Log Output

```
2026-01-06 10:00:00 - INFO - ✓ IjazahParser initialized - Ijazah akan di-parse otomatis
...
2026-01-06 10:01:00 - INFO - Parsing ijazah dengan OpenAI Vision API...
2026-01-06 10:01:02 - INFO - ✓ Ijazah parsed successfully
2026-01-06 10:01:02 - INFO - ✓ Successfully processed NIK 1234567890123456
2026-01-06 10:01:02 - INFO -   Bank: BANK BRI
2026-01-06 10:01:02 - INFO -   Rekening: 1234567890
2026-01-06 10:01:02 - INFO -   Pemilik: John Doe
2026-01-06 10:01:02 - INFO -   Ijazah Nama: John Doe
2026-01-06 10:01:02 - INFO -   Ijazah Gelar: S.Kom
2026-01-06 10:01:02 - INFO -   Universitas: Universitas Indonesia
```

---

## Support

Jika ada pertanyaan atau masalah, silakan buka issue di repository ini.
