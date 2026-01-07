# Fitur Mismatch Detection & Auto-Highlighting

## 🎯 Tujuan
Mendeteksi dan menandai secara otomatis baris-baris yang memiliki **potensi kesalahan data** (mismatch) antara Nama Pemilik Rekening dan Nomor Rekening.

---

## 🔍 Cara Kerja

### 1. **Deteksi Mismatch Saat Scraping**
Script akan otomatis memeriksa setiap nomor rekening yang di-scrape:

```python
# Validasi: Nomor rekening harus berisi angka saja
if no_rekening != "N/A" and not no_rekening.replace('-', '').replace(' ', '').isdigit():
    # MISMATCH DETECTED!
    logger.error(f"⚠ POTENTIAL MISMATCH DETECTED for NIK {nik_text}!")
```

**Kriteria Mismatch:**
- Nomor rekening mengandung **huruf** (contoh: "JOHN DOE", "BCA SYARIAH")
- Indikasi data tertukar antara nama dan nomor

---

### 2. **Logging Real-Time**
Saat mismatch terdeteksi, akan muncul warning di log:

```
⚠ POTENTIAL MISMATCH DETECTED for NIK 1234567890123456!
  Nomor Rekening contains non-numeric: 'JOHN DOE'
  Nama Pemilik: '1234567890'
  This data may be incorrect - please verify manually!
```

---

### 3. **Auto-Highlighting di Excel**

#### **Sheet "Summary"** (Tab pertama)
Berisi statistik data quality:
- Total rows scraped
- Jumlah rows dengan mismatch
- Data quality rate (%)
- Legend penjelasan warna

**Contoh:**
```
SCRAPING SUMMARY & DATA QUALITY REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Metric                      | Value
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Rows Scraped          | 100
Rows with Potential Mismatch| 3    ← Highlighted in RED
Data Quality Rate           | 97.0%
```

#### **Sheet "Data Mitra"** (Tab kedua)
- Baris **normal**: background putih
- Baris **mismatch**: background **merah muda/pink** (#FFC7CE)
- Kolom "Nomor Rekening" pada baris mismatch: **font merah bold** (#9C0006)

---

## 📊 Contoh Visual

### Normal Row (✅ OK):
| NIK | Nama | **Nomor Rekening** | Nama Bank | Nama Pemilik |
|-----|------|-------------------|-----------|--------------|
| 123...| John Doe, S.Kom | **1234567890** | BRI | JOHN DOE |

### Mismatch Row (🔴 ERROR):
| NIK | Nama | **Nomor Rekening** | Nama Bank | Nama Pemilik |
|-----|------|-------------------|-----------|--------------|
| 456...| Bob Wilson | **JOHN DOE** ⚠️ | BNI | 1234567890 |
> **Background: Pink, Font Nomor Rekening: Red Bold**

---

## 🧪 Testing

### Jalankan Test Script:
```bash
python test_mismatch_highlighting.py
```

Ini akan membuat file `sample_mismatch_highlighting.xlsx` dengan:
- 5 rows total
- 2 rows dengan mismatch (row 4 dan 6)
- Data quality: 60%

**Buka file Excel untuk melihat:**
1. Tab "Summary" dengan statistik
2. Tab "Data Mitra" dengan highlighting merah pada baris bermasalah

---

## 🚀 Penggunaan di Production

### 1. **Jalankan Scraper Normal**
```bash
python scrape_mitra.py
```

### 2. **Periksa Log**
Cari baris dengan `⚠ POTENTIAL MISMATCH DETECTED`

### 3. **Buka Excel Output**
- File: `output_YYYYMMDD_HHMMSS/mitra_data.xlsx`
- Buka tab "Summary" untuk lihat berapa banyak mismatch
- Buka tab "Data Mitra" dan **scroll ke baris merah**

### 4. **Verifikasi Manual**
Untuk setiap baris merah:
1. Buka website BPS manual
2. Cek NIK yang bermasalah
3. Catat nomor rekening yang benar
4. Update di Excel

---

## 🔧 Penyebab Mismatch

### **Root Cause:**
1. **Race Condition** - Tab Rekening belum fully loaded
2. **Fallback Parsing Error** - Salah tangkap baris
3. **Modal Tidak Tertutup** - Data tercampur antar NIK

### **Solusi yang Sudah Diimplementasi:**
✅ Wait eksplisit untuk konten tab Rekening  
✅ Verifikasi modal tertutup sebelum lanjut  
✅ Validasi data real-time  
✅ Auto-highlighting untuk identifikasi cepat  

---

## 📈 Statistik Improvement

| Metrik | Sebelum | Sesudah |
|--------|---------|---------|
| **Wait Strategy** | Blind 1.5s | Smart wait (max 8s) |
| **Mismatch Detection** | ❌ Manual | ✅ Otomatis |
| **Identifikasi Error** | 🐌 Lambat | ⚡ Real-time |
| **Excel Highlighting** | ❌ Tidak ada | ✅ Auto-highlight |

---

## 💡 Tips

1. **Jika banyak mismatch (>5%):**
   - Periksa koneksi internet
   - Tambah delay di `page.wait_for_timeout(800)` → `1500`
   - Jalankan ulang untuk NIK yang error saja

2. **False Positive:**
   - Beberapa bank punya format rekening dengan huruf (jarang)
   - Verifikasi manual tetap diperlukan

3. **Batch Processing:**
   - Untuk data besar, scrape per halaman
   - Periksa summary sheet setelah setiap batch

---

## 📝 Changelog

### v2.0 - Mismatch Detection (2026-01-07)
- ✅ Added real-time mismatch validation
- ✅ Added auto-highlighting in Excel (red/pink)
- ✅ Added Summary sheet with statistics
- ✅ Improved wait strategy for Rekening tab
- ✅ Added modal closure verification

### v1.0 - Initial Release
- Basic scraping functionality
- Excel/CSV export
- Ijazah parsing with OpenAI

---

## 🆘 Troubleshooting

**Q: Semua baris di-highlight merah?**  
A: Kemungkinan selector berubah. Periksa HTML structure website BPS.

**Q: Tidak ada highlighting sama sekali?**  
A: Berarti semua data valid! ✅ (atau validasi tidak berjalan - cek log)

**Q: File Excel corrupt?**  
A: Pastikan openpyxl versi terbaru: `pip install --upgrade openpyxl`

---

## 📧 Support

Jika menemukan bug atau punya saran improvement, silakan:
1. Cek log file: `scraper_YYYYMMDD_HHMMSS.log`
2. Screenshot baris yang error di Excel
3. Catat NIK yang bermasalah

---

**Happy Scraping! 🚀**
