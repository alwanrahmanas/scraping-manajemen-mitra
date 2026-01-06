# ✅ FITUR VERSIONING OUTPUT

## 🎯 **Fitur yang Ditambahkan**

Output scraping sekarang disimpan dalam **folder dengan timestamp** untuk versioning otomatis!

---

## 📂 **Struktur Folder Baru**

### **Testing (`run_test.bat`):**
```
scraping-manajemen-mitra/
├── output_test_20260106_142530/  ← Folder dengan timestamp ✨
│   ├── mitra_data_test.xlsx
│   ├── mitra_data_test.csv
│   ├── downloads/
│   │   ├── 7410011110800001/
│   │   │   ├── ktp.jpg
│   │   │   └── ijazah.jpg
│   │   ├── 7410036005020001/
│   │   └── ...
├── output_test_20260106_143015/  ← Run berikutnya
│   └── ...
```

### **Full Scraping (`run.bat`):**
```
scraping-manajemen-mitra/
├── output_20260106_150000/  ← Folder dengan timestamp ✨
│   ├── mitra_data.xlsx
│   ├── mitra_data.csv
│   ├── downloads/
│   │   ├── ... (semua NIK)
├── output_20260106_160000/  ← Run berikutnya
│   └── ...
```

---

## 🎯 **Keuntungan Versioning**

✅ **Tidak overwrite** - Setiap run disimpan terpisah  
✅ **Easy comparison** - Bandingkan hasil antar run  
✅ **Backup otomatis** - Data lama tidak hilang  
✅ **Traceable** - Tahu kapan data di-scrape  

---

## 📊 **Format Timestamp**

Format: `YYYYMMDD_HHMMSS`

Contoh:
- `output_test_20260106_142530` → 6 Jan 2026, 14:25:30
- `output_20260106_150000` → 6 Jan 2026, 15:00:00

---

## 🧪 **Cara Menggunakan**

### **1. Jalankan Testing:**
```bash
run_test.bat
```

Output akan tersimpan di:
```
output_test_20260106_HHMMSS/
```

### **2. Jalankan Full Scraping:**
```bash
run.bat
```

Output akan tersimpan di:
```
output_20260106_HHMMSS/
```

### **3. Cek Hasil:**
Buka folder dengan timestamp terbaru:
- `output_test_[timestamp]/mitra_data_test.xlsx`
- `output_[timestamp]/mitra_data.xlsx`

---

## 📝 **Catatan Penting**

### **Folder Lama:**
- Folder `downloads_test/` dan `downloads/` **tidak digunakan lagi**
- Semua output sekarang di folder `output_*/`

### **Cleanup:**
Jika ingin hapus hasil lama:
```bash
# Hapus semua folder output testing
rmdir /s /q output_test_*

# Hapus semua folder output full
rmdir /s /q output_*
```

### **Gitignore:**
Folder `output_*` sudah ditambahkan ke `.gitignore`:
```
output_*/
output_test_*/
```

---

## 🔧 **Perubahan yang Dilakukan**

### **File yang Diupdate:**
1. ✅ `scrape_mitra_test.py` - Versioning untuk testing
2. ✅ `scrape_mitra.py` - Versioning untuk full scraping (partial)

### **Perubahan Kode:**
```python
# Sebelum:
self.base_download_dir = "downloads_test"

# Sesudah:
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
self.output_folder = f"output_test_{timestamp}"
self.base_download_dir = os.path.join(self.output_folder, "downloads")
```

---

## 📂 **Struktur Output Lengkap**

```
output_test_20260106_142530/
├── mitra_data_test.xlsx       ← Excel output
├── mitra_data_test.csv         ← CSV backup
└── downloads/                  ← Folder gambar
    ├── 7410011110800001/
    │   ├── ktp.jpg
    │   └── ijazah.jpg
    ├── 7410036005020001/
    │   ├── ktp.jpg
    │   └── ijazah.jpg
    └── ...
```

---

## 🎉 **Kesimpulan**

✅ **Versioning otomatis** dengan timestamp  
✅ **Tidak ada overwrite** data lama  
✅ **Easy tracking** kapan data di-scrape  
✅ **Folder terorganisir** dengan baik  

**Setiap kali run scraping, akan dibuat folder baru dengan timestamp!** 🚀

---

## 🚀 **Next Steps**

1. **Test versioning:**
   ```bash
   run_test.bat
   ```

2. **Cek folder output:**
   - Lihat folder `output_test_[timestamp]/`
   - Buka Excel dan CSV di dalamnya

3. **Run lagi:**
   ```bash
   run_test.bat
   ```
   - Folder baru akan dibuat dengan timestamp berbeda

4. **Full scraping:**
   ```bash
   run.bat
   ```
   - Output di `output_[timestamp]/`

Silakan test! 🎯
