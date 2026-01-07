# 🔑 Cara Mendapatkan OpenAI API Key

> **Panduan lengkap untuk mendapatkan API key OpenAI (untuk parsing ijazah)**

---

## 📋 Langkah-Langkah

### **1. Buka Website OpenAI**

Klik link ini: https://platform.openai.com/api-keys

### **2. Login atau Daftar**

**Jika sudah punya akun:**
- Klik "Log in"
- Masukkan email dan password

**Jika belum punya akun:**
- Klik "Sign up"
- Daftar dengan email atau Google account
- Verifikasi email Anda

### **3. Buat API Key**

1. Setelah login, Anda akan lihat halaman "API keys"
2. Klik tombol **"Create new secret key"**
3. Beri nama (contoh: "Scraping Mitra BPS")
4. Klik **"Create secret key"**

### **4. Copy API Key**

⚠️ **PENTING:** API key hanya ditampilkan SEKALI!

1. Copy API key yang muncul (mulai dengan `sk-proj-...`)
2. Simpan di tempat aman (Notepad, dll)
3. Jangan share ke orang lain!

### **5. Setup di Project**

1. Buka folder project
2. Cari file **`.env.example`**
3. Copy file tersebut dan rename jadi **`.env`**
4. Buka file `.env` dengan Notepad
5. Ganti `your_api_key_here` dengan API key Anda:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

6. Simpan file

**✅ Selesai!** API key sudah siap digunakan.

---

## 💰 Biaya

### **Free Trial**

OpenAI memberikan **$5 credit gratis** untuk akun baru (berlaku 3 bulan).

### **Biaya Parsing Ijazah**

- Model yang digunakan: `gpt-4o-mini`
- Biaya per ijazah: ~$0.001 - $0.002
- Contoh:
  - 100 ijazah = ~$0.1-0.2
  - 500 ijazah = ~$0.5-1
  - 1000 ijazah = ~$1-2

### **Top Up**

Jika credit habis:
1. Buka: https://platform.openai.com/settings/organization/billing
2. Klik "Add payment method"
3. Masukkan kartu kredit
4. Set limit (misal: $10)

---

## 🔒 Keamanan API Key

### **✅ DO (Lakukan):**

- Simpan API key di file `.env`
- Jangan commit file `.env` ke Git (sudah ada di `.gitignore`)
- Ganti API key jika bocor

### **❌ DON'T (Jangan):**

- Share API key ke orang lain
- Upload API key ke GitHub
- Screenshot API key dan share
- Hardcode API key di script

---

## 🐛 Troubleshooting

### **Error: "Incorrect API key provided"**

**Penyebab:** API key salah atau expired

**Solusi:**
1. Cek file `.env`
2. Pastikan API key benar (copy-paste ulang)
3. Pastikan tidak ada spasi di awal/akhir
4. Jika masih error, buat API key baru

### **Error: "You exceeded your current quota"**

**Penyebab:** Credit OpenAI habis

**Solusi:**
1. Cek usage: https://platform.openai.com/usage
2. Top up credit jika perlu
3. Atau tunggu reset bulanan (jika pakai free trial)

### **Error: "Rate limit exceeded"**

**Penyebab:** Terlalu banyak request dalam waktu singkat

**Solusi:**
- Tunggu beberapa menit
- Coba lagi
- Jika sering terjadi, upgrade plan

---

## ❓ FAQ

### **Q: Apakah harus bayar?**

**A:** Tidak, jika masih punya free trial $5. Tapi jika habis, harus top up.

### **Q: Berapa lama free trial berlaku?**

**A:** 3 bulan sejak akun dibuat.

### **Q: Bisa pakai API key orang lain?**

**A:** Bisa, tapi tidak disarankan. Lebih baik buat sendiri.

### **Q: API key bisa dipakai berkali-kali?**

**A:** Ya, sampai Anda delete atau credit habis.

### **Q: Bisa ganti API key?**

**A:** Bisa. Buat API key baru, lalu ganti di file `.env`.

---

## 📞 Butuh Bantuan?

Jika ada masalah:
1. Screenshot error
2. Cek file `.env` sudah benar
3. Hubungi developer

---

**Selamat mencoba! 🚀**
