# 🧪 TESTING SCRIPT - 10 Orang

## 📋 Deskripsi

Script testing untuk scraping **hanya 10 orang pertama** sebelum menjalankan scraping penuh.

### **Kegunaan:**
✅ Testing apakah scraping berfungsi dengan baik  
✅ Testing parsing ijazah dengan OpenAI API  
✅ Verifikasi output Excel dan CSV  
✅ Cek kualitas data sebelum scraping semua  

---

## 🚀 Cara Menggunakan

### 1️⃣ **Start Chrome**
```bash
start_chrome.bat
```
Login ke website dan buka halaman "Seleksi Mitra"

### 2️⃣ **Run Testing**
```bash
run_test.bat
```

Script akan:
- Scraping **10 orang pertama** saja
- Download KTP dan Ijazah ke folder `downloads_test/`
- Parse ijazah dengan OpenAI Vision API
- Simpan hasil ke `mitra_data_test.xlsx` dan `mitra_data_test.csv`
- Generate log file `scraper_test_*.log`

### 3️⃣ **Cek Hasil**
Buka file:
- `mitra_data_test.xlsx` - Excel dengan 10 orang
- `downloads_test/` - Folder berisi KTP dan Ijazah

### 4️⃣ **Jika Berhasil**
Jalankan scraping penuh:
```bash
run.bat
```

---

## 📊 Output Testing

### **File yang Dihasilkan:**

| File | Deskripsi |
|------|-----------|
| `mitra_data_test.xlsx` | Excel dengan 10 orang (format profesional) |
| `mitra_data_test.csv` | CSV backup |
| `downloads_test/` | Folder berisi KTP dan Ijazah (10 orang) |
| `scraper_test_*.log` | Log file detail |

### **Kolom Excel:**
1. **NIK** - Nomor Induk Kependudukan
2. **Nama Lengkap (dengan Gelar)** - Dari parsing ijazah AI
3. **Nomor Rekening** - Nomor rekening bank
4. + 11 kolom tambahan

---

## 🎯 Perbedaan Testing vs Full

| Aspek | Testing (`run_test.bat`) | Full (`run.bat`) |
|-------|-------------------------|------------------|
| **Jumlah Data** | 10 orang pertama | Semua orang (semua halaman) |
| **Output Folder** | `downloads_test/` | `downloads/` |
| **Output Excel** | `mitra_data_test.xlsx` | `mitra_data.xlsx` |
| **Output CSV** | `mitra_data_test.csv` | `mitra_data.csv` |
| **Log File** | `scraper_test_*.log` | `scraper_*.log` |
| **Waktu** | ~2-3 menit | ~30-40 menit (tergantung jumlah) |

---

## 🔧 Konfigurasi

### **Mengubah Jumlah Testing:**

Edit file `scrape_mitra_test.py`, line ~591:
```python
# Testing dengan 10 orang pertama
scraper = MitraScraperTest(max_rows=10)  # ← Ubah angka ini
```

Contoh:
- `max_rows=5` → Testing 5 orang
- `max_rows=20` → Testing 20 orang
- `max_rows=50` → Testing 50 orang

---

## ✅ Checklist Testing

Setelah testing selesai, cek:

- [ ] File `mitra_data_test.xlsx` berisi 10 baris data
- [ ] Kolom **"Nama Lengkap (dengan Gelar)"** terisi (jika API key tersedia)
- [ ] Kolom **"Nomor Rekening"** terisi
- [ ] Folder `downloads_test/` berisi 10 subfolder (NIK)
- [ ] Setiap subfolder berisi `ktp.jpg` dan `ijazah.jpg`
- [ ] Log file tidak ada error fatal
- [ ] Parsing ijazah berfungsi (jika API key tersedia)

---

## 🐛 Troubleshooting

### **Error: "No data rows found"**
- Pastikan sudah login ke website
- Pastikan sudah di halaman "Seleksi Mitra"
- Tunggu halaman loading selesai

### **Parsing ijazah tidak jalan**
- Cek file `.env` berisi OpenAI API key
- Lihat log: "IjazahParser initialized" = berhasil
- Lihat log: "IjazahParser tidak aktif" = API key tidak ada

### **Download gambar gagal**
- Cek koneksi internet
- Lihat log untuk HTTP status code
- Beberapa gambar mungkin tidak tersedia

---

## 📝 Contoh Output Log

```
============================================================
MITRA BPS SCRAPER - TESTING MODE (Max 10 rows)
============================================================
✓ Connected to: Seleksi Mitra : Manajemen Mitra
✓ Found 10 data rows (limited to 10)

============================================================
Processing Row 1: NIK 7410011110800001
============================================================
✓ Popup opened
✓ Downloaded ktp.jpg (245.67 KB)
✓ Downloaded ijazah.jpg (312.45 KB)
Parsing ijazah dengan OpenAI Vision API...
✓ Ijazah parsed successfully
✓ Successfully processed NIK 7410011110800001
  Bank: BANK BRI
  Rekening: 707601025054539
  Pemilik: JOHN DOE
  Ijazah Nama: John Doe
  Ijazah Gelar: S.Kom
  Universitas: Universitas Indonesia

--- Progress: 1/10 ---

... (9 orang lagi) ...

============================================================
TESTING SUMMARY
============================================================
Max rows (limit): 10
Total rows processed: 10
✓ Successful: 10
✗ Failed: 0
📷 KTP downloaded: 10
📷 Ijazah downloaded: 10
📝 Ijazah parsed: 10
============================================================
```

---

## 🎉 Kesimpulan

Script testing ini membantu Anda:
1. ✅ Verifikasi scraping berfungsi dengan baik
2. ✅ Test parsing ijazah sebelum scraping semua
3. ✅ Hemat waktu dan biaya API (hanya 10 orang)
4. ✅ Cek kualitas output sebelum scraping penuh

**Jika testing berhasil, lanjutkan dengan `run.bat` untuk scraping semua data!** 🚀

---

## 📂 File Terkait

- `scrape_mitra_test.py` - Script testing (10 orang)
- `run_test.bat` - Batch script untuk run testing
- `scrape_mitra.py` - Script full (semua orang)
- `run.bat` - Batch script untuk run full
