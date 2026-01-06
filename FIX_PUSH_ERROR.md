# 🔧 PANDUAN PUSH KE GITHUB

## ⚠️ Error yang Terjadi

```
error: src refspec main does not match any
```

**Penyebab:** Branch `main` belum ada di repository lokal.

---

## ✅ SOLUSI

### **Opsi 1: Gunakan Script Baru (Recommended)**

```bash
push_simple.bat
```

Script ini akan:
1. ✅ Create branch `main` jika belum ada
2. ✅ Add semua file
3. ✅ Commit dengan message lengkap
4. ✅ Set remote GitHub
5. ✅ Force push

---

### **Opsi 2: Manual Command**

Jalankan command berikut satu per satu:

```bash
# 1. Create dan switch ke branch main
git checkout -B main

# 2. Add semua file
git add -A

# 3. Commit
git commit -m "feat: Major update - AI parsing, versioning, improved selectors"

# 4. Set remote (jika belum)
git remote add origin https://github.com/alwanrahmanas/scraping-manajemen-mitra.git

# 5. Force push
git push -f origin main
```

---

### **Opsi 3: Gunakan Master Branch**

Jika repository GitHub menggunakan `master` bukan `main`:

```bash
# 1. Create dan switch ke branch master
git checkout -B master

# 2. Add semua file
git add -A

# 3. Commit
git commit -m "feat: Major update - AI parsing, versioning, improved selectors"

# 4. Set remote
git remote add origin https://github.com/alwanrahmanas/scraping-manajemen-mitra.git

# 5. Force push
git push -f origin master
```

---

## 🔍 Cek Branch yang Ada

```bash
# Cek branch lokal
git branch

# Cek branch remote
git branch -r

# Cek semua branch
git branch -a
```

---

## 📝 Commit Message Lengkap

```
feat: Major update - AI parsing, versioning, improved selectors

- Add AI-powered ijazah parsing with OpenAI Vision API
- Add automatic versioning with timestamp folders
- Add jenis ijazah detection (SMA/SMK vs Perguruan Tinggi)
- Add regex cleaning for nomor rekening
- Fix KTP & Ijazah download selectors
- Fix tab selection (skip DevTools & fs-storage)
- Improve error handling & timeout handling
- Better selector strategies for tab navigation
- Update documentation with better structure
```

---

## 🚀 Quick Fix

**Cara tercepat:**

```bash
push_simple.bat
```

Atau manual:

```bash
git checkout -B main && git add -A && git commit -m "feat: Major update" && git push -f origin main
```

---

## ⚠️ Troubleshooting

### **Error: "remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/alwanrahmanas/scraping-manajemen-mitra.git
```

### **Error: "Permission denied"**
- Pastikan Anda sudah login ke GitHub
- Cek akses ke repository
- Gunakan HTTPS atau SSH sesuai konfigurasi

### **Error: "Updates were rejected"**
- Gunakan force push: `git push -f origin main`
- Atau pull dulu: `git pull origin main --allow-unrelated-histories`

---

## ✅ Verifikasi

Setelah push berhasil, cek:

1. **GitHub Repository:** https://github.com/alwanrahmanas/scraping-manajemen-mitra
2. **Commit History:** Pastikan commit terbaru ada
3. **Files:** Pastikan semua file ter-upload

---

## 📞 Jika Masih Error

Jalankan dan kirim output:

```bash
git status
git branch -a
git remote -v
```

---

**Silakan coba `push_simple.bat` terlebih dahulu!** 🚀
