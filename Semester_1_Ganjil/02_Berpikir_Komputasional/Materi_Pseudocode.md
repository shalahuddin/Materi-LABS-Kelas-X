# Materi Informatika: Pseudocode — Resep Logika Penyelesaian Masalah

*   **Mata Pelajaran:** Informatika · **Kelas X / Fase E** · **Semester Ganjil**
*   **Modul:** Modul 2 — Berpikir Komputasional (Searching) · **Minggu Ke-3**
*   **Prasyarat:** Minggu 2 — Konsep Linear & Binary Search
*   **Tujuan Belajar:** Mampu menyusun resep langkah logis (pseudocode) untuk menyelesaikan masalah pencarian dan kehidupan sehari-hari sebelum diimplementasikan ke pemrograman Python.

---

## 🌉 Jembatan Belajar: Kenapa Belajar Ini Lagi (KKA vs Informatika)?

Mungkin kamu bertanya-tanya: *"Di kelas **KKA (Koding dan Kecerdasan Artifisial)** kan sudah dijelaskan tentang pseudocode, kenapa di kelas **Informatika (IT)** kita bahas lagi?"*

Mari kita bedakan:
1.  **Di Kelas KKA:** Kamu belajar **penjelasan umum (definisi)** bahwa pseudocode adalah cara menuliskan algoritma. Fokusnya lebih kepada teori dasar.
2.  **Di Kelas Informatika (IT):** Kita langsung **mempraktikkannya** untuk memecahkan masalah logika nyata (seperti mencoret-coret langkah *Searching* di papan tulis kemarin) dan menjadikannya **jembatan wajib sebelum menulis kode Python minggu depan**. 

> 💡 **Ingat:** Pseudocode adalah coretan resep sebelum koki mulai memasak. Menulis program tanpa pseudocode bagaikan masak sup tanpa resep — bisa jadi asin, gosong, atau berantakan!

---

## 📱 Analogi: Menjelaskan Langkah ke Teman vs Komputer

Bayangkan kamu mendapatkan pesan WhatsApp dari temanmu: *"Tolong jelasin cara bikin akun game baru di HP dong."*
Maka kamu akan membalas dengan langkah-langkah yang urut dan jelas:
1. Buka Play Store / App Store.
2. Ketik nama game di kolom pencarian.
3. Tekan pasang (install).
4. Setelah selesai, buka aplikasinya lalu pilih "Daftar Akun Baru".
5. Masukkan email dan kata sandi baru.
6. Tekan tombol "Kirim/Mulai".

Menulis **pseudocode** itu persis seperti cara di atas! Bedanya, langkah tersebut ditulis dengan **kata kunci standar** agar komputer (dan orang lain) bisa memahaminya secara konsisten.

---

## 🪄 6 Kata Kunci Ajaib (Wajib Hafal)

Agar langkah kita bisa dibaca dengan standar oleh komputer, kita hanya butuh **6 kata kunci utama**:

| Kata Kunci | Kegunaan | Analogi Kasir Kantin |
| :--- | :--- | :--- |
| **`MULAI` / `SELESAI`** | Penanda awal dan akhir proses. | Kantin buka / Kantin tutup |
| **`BACA`** | Menerima data masuk dari pengguna (*Input*). | Tanya pembeli: "Berapa uangmu?" (`BACA uang`) |
| **`TULIS`** | Menampilkan hasil ke layar (*Output*). | Bilang ke pembeli: "Ini nasi gorengnya" |
| **`JIKA ... MAKA`** | Mengambil keputusan (*Percabangan/Kondisi*). | "Kalau uang cukup, beli nasgor. Kalau tidak, batalkan." |
| **`UNTUK ... SAMPAI`**| Mengulangi proses secara otomatis (*Looping*). | Melayani siswa dari antrean ke-1 sampai ke-10. |
| **`SELESAI JIKA / UNTUK`** | Penutup dari blok keputusan atau perulangan. | Tanda tutup blok instruksi agar tidak bercampur. |

---

## 🧪 Uji Coba Pertama: Kasus Kasir Kantin

Mari kita tulis logika kasir kantin sederhana dalam format pseudocode memakai kata kunci ajaib di atas:

```text
MULAI
  BACA uang              ← Komputer meminta input jumlah uang pembeli
  JIKA uang >= 15000 MAKA
    TULIS "Ini nasi gorengnya"
  LAINNYA
    TULIS "Maaf, uangmu kurang untuk beli nasi goreng"
  SELESAI JIKA
SELESAI
```

*   Tanda `←` dibaca **"diisi"** atau **"menyimpan nilai"** ke dalam sebuah variabel/nama.
*   Jika pembeli memasukkan angka `20000`, maka komputer akan memeriksa `20000 >= 15000` (Benar) dan menampilkan `"Ini nasi gorengnya"`.

---

## 🔁 Melakukan Pekerjaan Berulang: Menggunakan `UNTUK`

Misalkan kasir ingin menghitung total harga dari **3 barang** yang dibeli pelanggan secara berulang:

```text
MULAI
  totalBelanja ← 0                ← Mulai dengan keranjang kosong (0 rupiah)
  UNTUK i = 1 SAMPAI 3            ← Ulangi langkah di dalam blok sebanyak 3 kali
    BACA hargaBarang
    totalBelanja ← totalBelanja + hargaBarang
  SELESAI UNTUK                   ← Berhenti mengulang setelah barang ke-3
  TULIS totalBelanja
SELESAI
```
Di sini, variabel `i` bertugas menghitung putaran perulangan (mulai dari barang ke-1, ke-2, lalu ke-3).

---

## ⚠️ PENTING: Perbedaan Indeks Manusia (1-Based) vs Indeks Komputer (0-Based)

Salah satu hal yang sering membuat siswa bingung saat mulai belajar coding adalah cara berhitung indeks (urutan). 

Bayangkan kita punya daftar nama siswa: `["Andi", "Bima", "Rina"]`.
1.  **Indeks Manusia (1-Based):** Kita menghitung dari angka **1**.
    *   Siswa ke-1: Andi
    *   Siswa ke-2: Bima
    *   Siswa ke-3: Rina
    *   *Digunakan saat:* Logika awal, diskusi coret-coret di papan tulis, atau penjelasan lisan sehari-hari.
2.  **Indeks Komputer (0-Based):** Komputer menghitung dari angka **0**.
    *   Siswa ke-0: Andi
    *   Siswa ke-1: Bima
    *   Siswa ke-2: Rina
    *   *Digunakan saat:* Pemrograman komputer sungguhan (seperti bahasa **Python** yang akan kita pakai minggu depan!).

**Bagaimana penulisan perulangannya?**
*   **Versi 1-Based (Manusia):** `UNTUK i = 1 SAMPAI jumlahNama`
*   **Versi 0-Based (Komputer):** `UNTUK i = 0 SAMPAI jumlahNama - 1`

Sebagai calon programmer informatika, kamu harus terbiasa melihat kedua gaya ini. Di bawah ini kita akan membandingkan penulisan algoritma pencarian dalam versi indeks manusia dan versi persiapan coding komputer.

---

## 🕵️ Penerapan Kasus Nyata: Algoritma Pencarian (Searching)

Mari kita ubah pemecahan masalah pencarian yang kemarin kita coret-coret di papan tulis ke dalam bentuk pseudocode:

### A. Linear Search (Mencari Satu Per Satu dari Atas ke Bawah)

#### 1. Versi Indeks Manusia (1-Based) — *Cocok untuk logika sehari-hari*
```text
MULAI
  BACA daftarSiswa
  BACA targetNama
  posisiKetemu ← -1                          ← Diisi -1 sebagai tanda awal "Belum Ketemu"
  
  UNTUK i = 1 SAMPAI jumlahSiswa
    JIKA daftarSiswa[i] = targetNama MAKA
      posisiKetemu ← i                       ← Simpan urutan nomor siswa yang cocok
    SELESAI JIKA
  SELESAI UNTUK
  
  JIKA posisiKetemu = -1 MAKA
    TULIS "Nama tidak terdaftar di kelas"
  LAINNYA
    TULIS "Nama ditemukan di nomor urutan: ", posisiKetemu
  SELESAI JIKA
SELESAI
```

#### 2. Versi Persiapan Koding Komputer (0-Based) — *Sesuai dengan logika Python*
```text
MULAI
  BACA daftarSiswa
  BACA targetNama
  posisiKetemu ← -1
  
  UNTUK i = 0 SAMPAI jumlahSiswa - 1          ← Komputer mulai menghitung indeks dari 0
    JIKA daftarSiswa[i] = targetNama MAKA
      posisiKetemu ← i
    SELESAI JIKA
  SELESAI UNTUK
  
  JIKA posisiKetemu = -1 MAKA
    TULIS "Nama tidak ditemukan"
  LAINNYA
    TULIS "Nama ditemukan di indeks ke-", posisiKetemu
  SELESAI JIKA
SELESAI
```

---

### B. Binary Search (Mencari Pintar dengan Tebak Tengah)
*Syarat utama: Daftar nama harus sudah diurutkan dari A-Z terlebih dahulu.*

#### 1. Versi Indeks Manusia (1-Based)
```text
MULAI
  BACA daftarSiswa_terurut
  BACA targetNama
  kiri ← 1                                   ← Batas kiri adalah urutan pertama
  kanan ← jumlahSiswa                        ← Batas kanan adalah urutan terakhir
  posisiKetemu ← -1
  
  SELAMA kiri <= kanan
    tengah ← (kiri + kanan) / 2              ← Ambil posisi tengah (bulatkan ke bawah)
    JIKA daftarSiswa_terurut[tengah] = targetNama MAKA
      posisiKetemu ← tengah
      kiri ← kanan + 1                       ← Hentikan perulangan (memaksa kondisi salah)
    LAINNYA JIKA daftarSiswa_terurut[tengah] < targetNama MAKA
      kiri ← tengah + 1                      ← Buang bagian kiri, cari di kanan
    LAINNYA
      kanan ← tengah - 1                     ← Buang bagian kanan, cari di kiri
    SELESAI JIKA
  SELESAI SELAMA
  
  TULIS posisiKetemu                         ← Menampilkan hasil akhir (-1 jika tidak ada)
SELESAI
```

#### 2. Versi Persiapan Koding Komputer (0-Based)
```text
MULAI
  BACA daftarSiswa_terurut
  BACA targetNama
  kiri ← 0                                   ← Batas kiri dimulai dari indeks 0
  kanan ← jumlahSiswa - 1                    ← Batas kanan berakhir di indeks N-1
  posisiKetemu ← -1
  
  SELAMA kiri <= kanan
    tengah ← (kiri + kanan) / 2              (Bulatkan ke bawah jika ganjil)
    JIKA daftarSiswa_terurut[tengah] = targetNama MAKA
      posisiKetemu ← tengah
      kiri ← kanan + 1                       ← Hentikan pencarian karena sudah ketemu
    LAINNYA JIKA daftarSiswa_terurut[tengah] < targetNama MAKA
      kiri ← tengah + 1
    LAINNYA
      kanan ← tengah - 1
    SELESAI JIKA
  SELESAI SELAMA
  
  TULIS posisiKetemu
SELESAI
```

---

## 📝 5 Aturan Emas Menulis Pseudocode yang Baik

Agar tulisanmu rapi dan mudah dibaca oleh siapapun (termasuk komputer), ikuti 5 aturan penting ini:
1.  **Konsisten Bahasa:** Pilih satu bahasa (Bahasa Indonesia atau Inggris). Jangan campur-campur (misal: `JIKA` tapi di bawahnya memakai `else` atau `input`).
2.  **Satu Baris = Satu Aksi:** Jangan menumpuk banyak instruksi dalam satu baris kalimat.
3.  **Nama Variabel Jelas:** Beri nama penampung data secara deskriptif (misal: `hargaBarang` lebih baik daripada `hb` atau `x`).
4.  **Gunakan Indentasi (Menjorok ke Dalam):** Geser tulisan ke kanan untuk menunjukkan instruksi yang berada di dalam `JIKA` atau `UNTUK`. Ini sangat penting karena Python juga menggunakan sistem indentasi ini!
5.  **Tutup Apa yang Kamu Buka:** Setiap ada kata kunci pembuka seperti `MULAI`, `JIKA`, `UNTUK`, atau `SELAMA`, wajib ditutup dengan `SELESAI`, `SELESAI JIKA`, `SELESAI UNTUK`, atau `SELESAI SELAMA`.

---

## 🕵️ 5 Kesalahan Umum Pemula (Wajib Dihindari)

1.  **Variabel Misterius:** Memakai variabel tanpa kejelasan makna (seperti `a`, `b`, `c` untuk harga, jumlah, dan diskon).
2.  **Lupa Menutup Blok:** Lupa menulis `SELESAI JIKA` atau `SELESAI UNTUK` sehingga program tidak tahu di mana batas akhir keputusannya.
3.  **Mencampur Sintaks Bahasa Pemrograman:** Menuliskan titik koma `;`, kurung kurawal `{}`, atau tanda `==` yang khas di bahasa C++/Java. Tetap santai dan gunakan bahasa manusia.
4.  **Tidak Ada Indentasi:** Semua teks rata kiri sehingga sangat melelahkan dibaca.
5.  **Terlalu Panjang & Detail:** Menuliskan instruksi non-logika seperti *"Ambil pulpen lalu letakkan di atas meja"* — fokus saja ke proses data.

---

## 📌 Cheat Sheet (Ringkasan Cepat)

*   `MULAI` / `SELESAI` : Awal & Akhir Program
*   `BACA [nama]` : Meminta Masukan (*Input*)
*   `TULIS [nama]` : Menampilkan Informasi (*Output*)
*   `←` : Tanda diisi nilai (*Assignment*)
*   `JIKA ... MAKA ... LAINNYA ... SELESAI JIKA` : Percabangan Keputusan
*   `UNTUK ... SAMPAI ... SELESAI UNTUK` : Perulangan dengan jumlah pasti
*   `SELAMA ... SELESAI SELAMA` : Perulangan dengan kondisi syarat

---

## ✍️ Latihan HOTS (Higher Order Thinking Skills)

Kerjakan soal di bawah ini untuk menguji ketajaman logikamu sebelum membuat program di komputer!

### 🔍 Soal 1 — Menganalisis (Menemukan Error Logika)
Perhatikan pseudocode untuk mencari nilai terbesar dari sekumpulan angka berikut:
```text
MULAI
  BACA daftarAngka
  terbesar ← 0
  UNTUK i = 1 SAMPAI jumlahAngka
    JIKA daftarAngka[i] > terbesar MAKA
      terbesar ← daftarAngka[i]
    SELESAI JIKA
  SELESAI UNTUK
  TULIS terbesar
SELESAI
```
**Pertanyaan:** Apakah algoritma ini akan berfungsi dengan benar jika semua angka di dalam `daftarAngka` bernilai negatif (misalnya suhu di kutub utara: `[-8, -3, -15]`)? Analisis apa yang terjadi, dan tuliskan perbaikannya.
<details>
<summary><b>🔍 Lihat Kunci Jawaban & Pembahasan</b></summary>

**Analisis:**
Algoritma ini akan **salah** jika semua nilai berupa angka negatif. 
Karena nilai awal `terbesar` diisi dengan `0`, komputer akan membandingkan `-8 > 0` (Salah), `-3 > 0` (Salah), dan `-15 > 0` (Salah). Output yang ditampilkan adalah `0`, padahal `0` tidak ada di dalam daftar angka tersebut dan suhu terbesar aslinya adalah `-3`.

**Perbaikan:**
Inisialisasikan variabel `terbesar` dengan mengambil elemen pertama dari daftar angka tersebut, bukan angka `0`.
```text
MULAI
  BACA daftarAngka
  terbesar ← daftarAngka[1]                   ← Mengambil elemen pertama sebagai acuan
  UNTUK i = 2 SAMPAI jumlahAngka              ← Mulai membandingkan dari elemen ke-2
    JIKA daftarAngka[i] > terbesar MAKA
      terbesar ← daftarAngka[i]
    SELESAI JIKA
  SELESAI UNTUK
  TULIS terbesar
SELESAI
```
</details>

---

### 🛠️ Soal 2 — Menciptakan (Membuat Algoritma Diskon Kasir)
Buatlah sebuah pseudocode untuk sistem kasir minimarket. Program harus meminta masukan total belanjaan pelanggan. 
*   Jika total belanjaan mencapai **Rp100.000 atau lebih**, pelanggan mendapatkan **diskon 10%** dari total belanjaannya. 
*   Program kemudian menampilkan nominal diskon yang didapat dan total akhir yang harus dibayar setelah dikurangi diskon.
*   *Pengembangan:* Tuliskan juga versi yang mengulangi input harga barang sebanyak **3 barang** terlebih dahulu sebelum menghitung total belanja.
<details>
<summary><b>🔍 Lihat Kunci Jawaban & Pembahasan</b></summary>

**Versi Sederhana (Satu input total belanja):**
```text
MULAI
  BACA totalBelanja
  JIKA totalBelanja >= 100000 MAKA
    diskon ← totalBelanja * 0.1
  LAINNYA
    diskon ← 0
  SELESAI JIKA
  totalBayar ← totalBelanja - diskon
  TULIS "Diskon didapat: Rp", diskon
  TULIS "Total bayar: Rp", totalBayar
SELESAI
```

**Versi Pengembangan (Menggunakan Perulangan untuk 3 Barang):**
```text
MULAI
  totalBelanja ← 0
  UNTUK i = 1 SAMPAI 3
    TULIS "Masukkan harga barang ke-", i
    BACA hargaBarang
    totalBelanja ← totalBelanja + hargaBarang
  SELESAI UNTUK
  
  JIKA totalBelanja >= 100000 MAKA
    diskon ← totalBelanja * 0.1
  LAINNYA
    diskon ← 0
  SELESAI JIKA
  
  totalBayar ← totalBelanja - diskon
  TULIS "Total Belanja Sebelum Diskon: Rp", totalBelanja
  TULIS "Diskon 10% Didapat: Rp", diskon
  TULIS "Total Yang Harus Dibayar: Rp", totalBayar
SELESAI
```
</details>

---

### ⚖️ Soal 3 — Mengevaluasi (Memilih Algoritma Terbaik)
Dua orang siswa kelas X Informatika berdebat tentang cara mendeteksi apakah sebuah bilangan bulat merupakan bilangan genap atau ganjil.

*   **Siswa A menulis:**
    ```text
    JIKA angka / 2 = bilangan bulat MAKA
      TULIS "Bilangan Genap"
    LAINNYA
      TULIS "Bilangan Ganjil"
    SELESAI JIKA
    ```
*   **Siswa B menulis:**
    ```text
    JIKA angka MOD 2 = 0 MAKA
      TULIS "Bilangan Genap"
    LAINNYA
      TULIS "Bilangan Ganjil"
    SELESAI JIKA
    ```

**Pertanyaan:** Berikan penilaianmu, algoritma milik siswa mana yang lebih jelas dan aman dari kesalahan ketika diprogram ke dalam komputer? Jelaskan alasan logismu!
<details>
<summary><b>🔍 Lihat Kunci Jawaban & Pembahasan</b></summary>

**Evaluasi:**
Algoritma milik **Siswa B** jauh lebih jelas dan aman dari kesalahan komputer.

**Alasan:**
1.  **Kemudahan Terjemahan Komputer:** Komputer memiliki operator khusus bernama `MOD` (Modulo/sisa pembagian) yang langsung menghasilkan sisa pembagian bilangan bulat secara pasti (misal: `7 MOD 2 = 1` sedangkan `8 MOD 2 = 0`).
2.  **Kekaburan Logika Siswa A:** Siswa A menggunakan istilah `"bilangan bulat"`. Komputer tidak tahu secara langsung cara mengecek apakah hasil pembagian merupakan bilangan bulat atau bukan kecuali harus dibuat program pengecekan tipe data tambahan. Operasi pembagian biasa `/` pada komputer sering menghasilkan bilangan pecahan desimal (misal `7 / 2 = 3.5`), yang bisa memicu galat logika pada tipe data integer.
</details>

---

### 🛠️ Soal 4 — Menciptakan (Mengubah Langkah Manual Menjadi Perulangan)
Kamu diminta membuat algoritma untuk membuat kopi susu instan di sebuah kedai. Langkah manualnya adalah:
1. Masukkan kopi instan ke gelas.
2. Tuang susu kental manis.
3. Tuang air panas.
4. Aduk hingga rata.

Ubah langkah manual di atas menjadi pseudocode yang **bisa membuatkan kopi susu secara otomatis sebanyak jumlah gelas yang diminta oleh pembeli**.
<details>
<summary><b>🔍 Lihat Kunci Jawaban & Pembahasan</b></summary>

```text
MULAI
  TULIS "Berapa gelas kopi susu yang ingin dibuat?"
  BACA jumlahPesanan
  
  UNTUK gelas = 1 SAMPAI jumlahPesanan
    TULIS "Membuat kopi susu untuk gelas ke-", gelas
    Masukkan kopi instan ke gelas
    Tuang susu kental manis
    Tuang air panas
    Aduk hingga rata
    TULIS "Gelas ke-", gelas, " selesai dibuat!"
  SELESAI UNTUK
  
  TULIS "Semua pesanan selesai dibuat! Siap disajikan."
SELESAI
```
</details>

---

### ⚖️ Soal 5 — Mengevaluasi (Menilai Kondisi Penggunaan Linear vs Binary)
Dalam kehidupan sehari-hari atau pembuatan program, kapan metode **Linear Search** (pencarian satu per satu dari awal) justru lebih baik atau lebih masuk akal dipilih dibandingkan dengan **Binary Search** (pencarian tebak tengah)? Sebutkan minimal 2 kondisi dan berikan alasannya!
<details>
<summary><b>🔍 Lihat Kunci Jawaban & Pembahasan</b></summary>

**Evaluasi Kondisi:**
Linear Search lebih unggul dan tepat dipilih pada kondisi berikut:

1.  **Daftar Data Belum Terurut (Acak):** Binary Search **wajib** menggunakan data yang sudah berurutan (misalnya A-Z atau 1-100). Jika datanya berantakan dan proses pengurutan (*sorting*) memakan waktu lama atau memori besar, lebih baik kita langsung melakukan Linear Search saja.
2.  **Jumlah Data Sangat Sedikit:** Jika data yang dicari hanya ada 3 sampai 5 elemen (misalnya mencari kontak darurat keluarga), kecepatan Binary Search tidak akan terasa berbeda dengan Linear Search. Linear Search lebih mudah ditulis kodenya dan lebih hemat memori komputer.
3.  **Proses Pencarian Jarang Dilakukan:** Jika kita hanya mencari data sekali saja dalam setahun, tidak sebanding jika kita harus meluangkan waktu menulis algoritma pengurutan data yang rumit untuk bisa menggunakan Binary Search.
</details>
