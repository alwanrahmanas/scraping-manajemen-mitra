# 📊 OUTPUT EXCEL - STRUKTUR FINAL

## ✅ Kolom Excel Hasil Scraping

### **KOLOM UTAMA (Prioritas Tinggi)**

| No | Kolom | Sumber Data | Keterangan |
|----|-------|-------------|------------|
| 1 | **NIK** | Scraping tabel | Nomor Induk Kependudukan |
| 2 | **Nama Lengkap (dengan Gelar)** | **Parsing Ijazah (AI)** | Nama + gelar lengkap (contoh: "John Doe, S.Kom") |
| 3 | **Nomor Rekening** | Scraping tab Rekening | Nomor rekening bank |

### **KOLOM TAMBAHAN (Nice to Have)**

| No | Kolom | Sumber Data | Keterangan |
|----|-------|-------------|------------|
| 4 | Nama Bank | Scraping tab Rekening | Nama bank (contoh: "BANK BRI") |
| 5 | Nama Pemilik Rekening | Scraping tab Rekening | Nama pemilik rekening |
| 6 | Gelar | **Parsing Ijazah (AI)** | Gelar saja (S.Kom, S.T., dll) |
| 7 | NIM | **Parsing Ijazah (AI)** | Nomor Induk Mahasiswa |
| 8 | Program Studi | **Parsing Ijazah (AI)** | Program studi (Teknik Informatika, dll) |
| 9 | Fakultas | **Parsing Ijazah (AI)** | Fakultas (Teknik, MIPA, dll) |
| 10 | Universitas | **Parsing Ijazah (AI)** | Nama universitas lengkap |
| 11 | Tanggal Ijazah | **Parsing Ijazah (AI)** | Tanggal penerbitan ijazah |
| 12 | Path KTP | Download | Path file KTP yang didownload |
| 13 | Path Ijazah | Download | Path file ijazah yang didownload |
| 14 | Status | System | Status processing (Success/Failed) |

---

## 📋 Contoh Output Excel

| NIK | Nama Lengkap (dengan Gelar) | Nomor Rekening | Nama Bank | Nama Pemilik Rekening | Gelar | NIM | Program Studi | Fakultas | Universitas | Tanggal Ijazah | Path KTP | Path Ijazah | Status |
|-----|----------------------------|----------------|-----------|---------------------|-------|-----|---------------|----------|-------------|----------------|----------|-------------|--------|
| 7410011110800001 | John Doe, S.Kom | 707601025054539 | BANK BRI | JOHN DOE | S.Kom | 1234567890 | Teknik Informatika | Teknik | Universitas Indonesia | 2020-08-15 | downloads/7410.../ktp.jpg | downloads/7410.../ijazah.jpg | Success |
| 7410030107670045 | Jane Smith, S.T. | 123456789012 | BANK BCA | JANE SMITH | S.T. | 0987654321 | Teknik Sipil | Teknik | Institut Teknologi Bandung | 2019-07-20 | downloads/7410.../ktp.jpg | downloads/7410.../ijazah.jpg | Success |

---

## 🎯 Fokus Utama

Sesuai permintaan Anda, **3 kolom utama** yang paling penting:

1. ✅ **NIK** - Identitas unik
2. ✅ **Nama Lengkap (dengan Gelar)** - Dari parsing ijazah dengan AI
3. ✅ **Nomor Rekening** - Untuk pembayaran

**Kolom lainnya** adalah **bonus/nice to have** untuk informasi tambahan.

---

## 🤖 Parsing Ijazah dengan AI

Kolom **"Nama Lengkap (dengan Gelar)"** diisi otomatis dari hasil parsing ijazah menggunakan **OpenAI Vision API (GPT-4o-mini)**.

### Cara Kerja:
1. Script download foto ijazah
2. Foto dikirim ke OpenAI Vision API
3. AI membaca dan mengekstrak informasi
4. Hasil disimpan ke Excel

### Jika Parsing Gagal:
- Kolom akan berisi **"N/A"**
- Script tetap lanjut (tidak crash)
- Foto ijazah tetap tersimpan di folder downloads

### Jika API Key Tidak Ada:
- Parsing di-skip
- Kolom ijazah berisi **"N/A"**
- Script tetap berjalan normal (hanya download)

---

## 📊 Format Excel

### Header
- **Background**: Biru (#4472C4)
- **Font**: Putih, Bold, Size 12
- **Alignment**: Center

### Data Rows
- **Auto-width columns**: Otomatis menyesuaikan lebar
- **Borders**: Semua cell ada border
- **Encoding**: UTF-8 (support karakter Indonesia)

### Sheet Name
- **"Data Mitra"**

---

## 💾 File Output

### 1. Excel: `mitra_data.xlsx`
- Format: Excel 2007+ (.xlsx)
- Formatting: Profesional dengan warna dan border
- **Recommended untuk analisis data**

### 2. CSV: `mitra_data.csv`
- Format: CSV UTF-8
- Backup plain text
- **Recommended untuk import ke sistem lain**

### 3. Folder Downloads: `downloads/`
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

---

## 🎯 Ringkasan

✅ **3 Kolom Utama**: NIK, Nama Lengkap (dengan Gelar), Nomor Rekening  
✅ **11 Kolom Tambahan**: Info bank, pendidikan, dan file paths  
✅ **Format Profesional**: Excel dengan formatting cantik  
✅ **Parsing AI**: Otomatis ekstrak nama dan gelar dari ijazah  
✅ **Robust**: Tetap jalan meski parsing gagal  

---

**File ini akan di-generate otomatis** setiap kali Anda menjalankan:
```bash
python scrape_mitra_no_pandas.py
```

atau

```bash
run_minimal.bat
```
