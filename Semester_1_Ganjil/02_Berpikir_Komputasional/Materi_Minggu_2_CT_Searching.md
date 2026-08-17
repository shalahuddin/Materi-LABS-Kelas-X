# Materi Minggu 2: Cara Mencari yang Pintar (Searching)

*   **Mapel:** Informatika · **Kelas X / Fase E** · **Semester Ganjil**
*   **Modul:** Modul 2 — Berpikir Komputasional
*   **Cara belajar:** Baca → coba contoh → kerjakan Lembar Aktivitas
*   **Bukan coding dulu:** minggu ini kita latih **cara berpikir**, belum bikin program Python

---

## Yuk Mulai dari yang Kamu Sudah Tahu

Pikirkan 10 detik:

> Kamu buka HP, ada ratusan kontak. Kamu mau chat **“Raka”**.  
> Apa yang kamu lakukan?

Sebagian orang scroll dari atas.  
Sebagian ketik di kotak pencarian.  
Sebagian buka huruf **R** dulu.

Tanpa sadar, kamu sudah pakai **cara mencari**.

Di Informatika, cara mencari yang rapi disebut **searching** (pencarian).  
Bukan “asal cari”, tapi **ada aturannya** supaya:

1. hasilnya **benar**,
2. prosesnya **bisa diulang** orang lain,
3. kalau bisa, **lebih cepat**.

> **Inti minggu ini (ingat ini saja dulu):**  
> *Mencari itu gampang. Yang pintar: mencari dengan aturan yang jelas.*

---

## 1. Apa Itu Searching? (Bahasa Gampang)

**Searching** = proses **menemukan sesuatu** di dalam kumpulan data.

Contoh di hidupmu:

| Situasi | Yang dicari (target) | Tempat mencari (data) |
| :--- | :--- | :--- |
| Chat teman | Nama “Raka” | Daftar kontak HP |
| PR Bahasa | Arti kata “efisien” | Kamus / KBBI |
| Absen kelas | Namamu | Daftar absensi |
| Ngerjain file | `tugas_mtk.docx` | Folder laptop |
| Di tas berantakan | Dompet | Isi tas |

### Cara komputer “mengerti” pencarian

Bayangkan seperti mesin sederhana:

```
MASUKAN  →  daftar data + apa yang dicari
PROSES   →  cek satu per satu (atau dengan cara lain) menurut aturan
HASIL    →  “ketemu di posisi ke-…”  atau  “tidak ada”
```

Kalau **aturan ceknya tidak jelas**, hasilnya bisa kacau:  
bisa kelewatan, bisa dobel cek, bisa bilang “tidak ada” padahal ada.

---

## 2. Kenapa Pakai Berpikir Komputasional?

**Berpikir komputasional (CT)** = cara memecahkan masalah secara rapi, mirip cara merancang solusi untuk komputer — tapi dikerjakan manusia dulu.

Ada **4 alat** (sering disebut 4 pilar). Saat mencari, keempatnya ikut kerja:

| Alat CT | Artinya sederhana | Saat kamu mencari nama |
| :--- | :--- | :--- |
| **Dekomposisi** | Pecah masalah jadi langkah kecil | 1) tentukan nama 2) buka daftar 3) cek 4) bilang hasil |
| **Pengenalan pola** | Cari kebiasaan yang berulang | Tiap nama dicek dengan cara yang sama |
| **Abstraksi** | Buang yang tidak penting | Yang dibandingkan cuma **nama**, bukan foto/status WA |
| **Algoritma** | Susun langkah berurutan | “Mulai dari atas, cek, kalau belum cocok lanjut…” |

### Contoh super dekat: cari kata “KOMPUTER” di daftar kosakata

1. **Pecah masalah:** siapkan daftar → tentukan kata target → tentukan cara cek → tentukan kapan berhenti.
2. **Pola:** semua kata dicek dengan aturan sama (misalnya semua huruf besar).
3. **Saring info:** yang dibanding ejaannya saja, bukan artinya.
4. **Langkah:** pilih cara **Linear** (daftar acak) atau **Binary** (daftar sudah A–Z).

Kalau 4 alat ini dipakai, searching tidak lagi “feeling”, tapi **bisa diajarkan ke orang lain** (bahkan nanti ke komputer).

---

## 3. Enam Aturan Main Sebelum Mencari

Sebelum “cek-cek”, setujui dulu **aturan main**. Ini mirip peraturan game — biar adil.

### Aturan 1 — Target harus jelas
*   ✅ Cari kata: `ALGORITMA`
*   ❌ Cari: “yang berhubungan sama algoritma” (terlalu kabur)

### Aturan 2 — Samakan bentuk tulisan
`Algoritma`, `ALGORITMA`, dan `algoritma` harus dianggap **sama**.  
Trik gampang: ubah semua jadi **HURUF BESAR** dulu.

### Aturan 3 — Tentukan arah cek
Contoh: dari kiri ke kanan, dari atas ke bawah, dari A ke Z.  
Jangan loncat-loncat tanpa aturan.

### Aturan 4 — Kapan bilang “ketemu”?
Minggu ini kita pakai **sama persis**.  
`PENSIL` = `PENSIL` → ketemu.  
`PENSIL` ≠ `PENSIL WARNA` → belum ketemu.

### Aturan 5 — Kapan berhenti?
*   Ketemu → **stop**, catat posisinya.
*   Sudah habis daftar → bilang **tidak ditemukan**.

### Aturan 6 — Hitung berapa kali kamu cek
Setiap kali membandingkan 1 data dengan target = **1 perbandingan**.  
Semakin sedikit (dengan tetap benar), semakin efisien.

> **Tips:** Aturan 1–6 ini yang membedakan “cari asal-asalan” dengan “algoritma pencarian”.

---

## 4. Cara 1: Linear Search (Cek Satu-satu)

### Ide sederhananya
Seperti mengantri mengecek isi laci dari depan ke belakang.

**Buka data pertama → cocok?  
Tidak → buka berikutnya → cocok?  
…  
Sampai ketemu atau data habis.**

### Kapan cocok dipakai?
*   Data **masih acak** (belum diurutkan A–Z).
*   Data **sedikit**.
*   Kamu cuma butuh cara yang **paling gampang**.

### Analogi yang gampang diingat
*   Nyari kunci di kotak berisi banyak kunci campur.
*   Nyari nama di absen yang **belum** diurut abjad.
*   Nyari catatan di kertas coret-coretan.

### Langkahnya (hapalkan alurnya, bukan hafalan kaku)
1. Mulai dari data **paling awal**.
2. Bandingkan dengan target.
3. Sama → **ketemu**, catat posisinya, berhenti.
4. Beda → geser ke data berikutnya.
5. Sudah di ujung dan belum ketemu → **tidak ditemukan**.

### Contoh diikuti pelan-pelan

Daftar (acak):

| Posisi | 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Kata | BUKU | PENSIL | PENGHAPUS | PENGGARIS | TAS |

Target: **PENGHAPUS**

```
Cek posisi 0: BUKU      ≠ PENGHAPUS  → lanjut
Cek posisi 1: PENSIL    ≠ PENGHAPUS  → lanjut
Cek posisi 2: PENGHAPUS = PENGHAPUS  → KETEMU di posisi 2
```

Jumlah cek = **3 kali**.

### Seberapa “capek” Linear Search?

Bayangkan daftar panjangnya **n** data.

| Situasi | Arti di kehidupan | Berapa kali cek? |
| :--- | :--- | :--- |
| Paling beruntung | Target ada di paling depan | 1 kali |
| Biasa saja | Target di sekitar tengah | kira-kira n/2 |
| Paling sial | Target di paling belakang / tidak ada | n kali (cek semua) |

Jadi: **makin panjang daftar, makin rawan lama** kalau cuma andalkan Linear.

### Pseudocode (bacanya seperti resep, belum wajib coding)
```
ALGORITMA CariLinear(daftar, target)
  untuk setiap posisi i dari awal sampai akhir:
    jika daftar[i] sama dengan target:
      kembalikan i          ← ketemu
  kembalikan "tidak ketemu"
```

---

## 5. Cara 2: Binary Search (Potong Setengah)

### Ide sederhananya
Seperti main **tebak angka**:

> Angka rahasia 1–100.  
> Kamu tebak 50. Guru bilang: “terlalu kecil”.  
> Berarti 1–50 dibuang. Sisa 51–100.  
> Tebak tengahnya lagi…  
> Terus memotong sampai ketemu.

Itu **Binary Search**.

### Syarat WAJIB (jangan sampai lupa)
Data harus **sudah rapi / terurut**.  
Contoh: A → Z, atau angka kecil → besar.

Kalau data masih acak lalu dipaksa Binary, hasilnya bisa **salah**.  
Ibarat pakai kamus yang halaman-halamannya diacak — loncat ke tengah jadi tidak ada artinya.

### Analogi gampang
*   Cari kata di **kamus / KBBI** (buka tengah, lihat abjad, buang sisi yang salah).
*   Cari **halaman 128** di buku 300 halaman.
*   Game tebak angka dengan petunjuk “terlalu kecil / terlalu besar”.

### Langkahnya (bahasa manusia)
1. Pastikan daftar **sudah terurut**.
2. Tandai ujung kiri dan ujung kanan area yang masih mungkin.
3. Ambil data di **tengah**.
4. Bandingkan dengan target:
   *   **Sama** → ketemu, selesai.
   *   Target “sebelum” data tengah (lebih awal abjad) → buang **sebelah kanan**.
   *   Target “sesudah” data tengah → buang **sebelah kiri**.
5. Ulangi di sisa data yang masih aktif.
6. Kalau area pencarian habis → tidak ditemukan.

### Contoh diikuti pelan-pelan

Daftar **sudah A–Z**:

| Posisi | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Kata | ALGORITMA | DATA | KOMPUTER | LOGIKA | PROGRAM | SEARCH | VARIABEL |

Target: **PROGRAM**

```
Langkah 1:
  kiri=0, kanan=6, tengah=3 → LOGIKA
  PROGRAM ada SETELAH LOGIKA → buang kiri, sekarang kiri=4

Langkah 2:
  kiri=4, kanan=6, tengah=5 → SEARCH
  PROGRAM ada SEBELUM SEARCH → buang kanan, sekarang kanan=4

Langkah 3:
  kiri=4, kanan=4, tengah=4 → PROGRAM
  SAMA → KETEMU di posisi 4
```

Jumlah cek = **3 kali**.  
Kalau pakai Linear dari kiri, untuk `PROGRAM` di daftar ini bisa butuh **5 cek**.

### Seberapa hebat potong-setengah?

| Jumlah data | Linear (kasus sial) | Binary (kira-kira) |
| :---: | :---: | :---: |
| 8 | sampai 8 cek | sekitar 3 cek |
| 16 | sampai 16 cek | sekitar 4 cek |
| 100 | sampai 100 cek | sekitar 7 cek |
| 1000 | sampai 1000 cek | sekitar 10 cek |

Intinya: **Binary tumbuh jauh lebih pelan** saat data membesar — **asal data sudah terurut**.

### Pseudocode (resep ringkas)
```
ALGORITMA CariBinary(daftar_terurut, target)
  kiri  = awal
  kanan = akhir
  selama kiri masih <= kanan:
    tengah = (kiri + kanan) bagi 2 (bulatkan ke bawah)
    jika daftar[tengah] == target → kembalikan tengah
    jika daftar[tengah] < target  → kiri  = tengah + 1
    jika daftar[tengah] > target  → kanan = tengah - 1
  kembalikan "tidak ketemu"
```

---

## 6. Kapan Pakai yang Mana? (Paling Sering Ditanya)

| Pertanyaan | Linear | Binary |
| :--- | :--- | :--- |
| Data harus terurut? | Tidak | **Ya** |
| Cara kerja | Cek berurutan | Potong setengah |
| Data kecil & acak | ✅ Paling praktis | Biasanya tidak perlu |
| Data besar & sudah rapi | Lambat | ✅ Lebih unggul |
| Gampang dipahami? | Sangat gampang | Perlu latihan sedikit |
| Analogi | Catatan berantakan | Kamus rapi |

### Pohon keputusan super singkat
```
Apakah data sudah terurut (A–Z / kecil→besar)?
   │
   ├─ BELUM  → pakai Linear Search
   │
   └─ SUDAH  → lebih baik Binary Search
               (apalagi kalau datanya banyak)
```

> **Jangan hafal “Binary selalu juara”.**  
> Kalau datanya cuma 5 item acak di tas, Linear jauh lebih masuk akal.

---

## 7. Aktivitas Kelas (Tanpa Coding)

### A. Cari Kartu Nama (latih Linear)
1. Siapkan 10–15 kartu nama **acak**.
2. Teman sebut 1 nama target.
3. Cek dari kiri ke kanan.
4. Hitung: ketemu di posisi berapa? Berapa kali kartu dibuka?

### B. Kamus Mini (latih Binary)
1. 15 kata **sudah diurut A–Z**.
2. Cari target **hanya lewat posisi tengah**.
3. Tiap langkah, coret sisi yang dibuang.
4. Bandingkan jumlah langkah dengan cara Linear.

### C. Tebak Angka 1–100 (rasakan ide Binary)
*   Guru simpan angka rahasia.
*   Jawaban hanya: terlalu kecil / terlalu besar / benar.
*   Target tantangan: ketemu dalam **maksimal 7 tebakan**.

---

## 8. 5 Kesalahan yang Sering Muncul (Biar Kamu Hindari)

1. **Paksa Binary di data acak** → jawaban bisa salah total.
2. **Lupa samakan huruf** (`Data` vs `data`) → dikira tidak ada.
3. **Salah hitung posisi tengah**, atau lupa geser kiri/kanan.
4. **Sudah ketemu tapi masih cek terus** → buang-buang langkah.
5. **Pikir Binary selalu terbaik** — padahal data kecil/acak lebih cocok Linear.

---

## 9. Latihan Cepat (Cek Pemahaman Sendiri)

Coba jawab tanpa mencontek dulu:

1. Searching itu apa, dalam 1 kalimat?
2. Sebutkan 3 dari 6 aturan mencari kata.
3. Data absensi belum diurut — pakai Linear atau Binary? Mengapa?
4. Mencari kata di KBBI lebih mirip Linear atau Binary? Mengapa?
5. Kenapa menghitung “berapa kali cek” itu penting?

*(Kunci singkat di benak guru: 1=menemukan data dengan aturan; 3=Linear; 4=Binary; 5=ukur efisiensi.)*

---

## 10. Hubungan ke Minggu Lain

```
Minggu 1                Minggu 2                     Minggu 3
Kerja kelompok   →   Cara mencari yang pintar   →   Dekomposisi lebih dalam
(kolaborasi)         (Linear vs Binary + CT)        (pecah masalah lebih rapi)
```

Bekal minggu ini:  
**algoritma = langkah yang jelas + bisa diukur.**  
Nanti di semester ini, langkah yang sama bisa kamu tulis jadi program.

---

## 🎮 Media & Latihan Tambahan

**File di folder minggu ini (buka pakai Chrome/Edge):**
1. `Slide_Interaktif_Minggu_2.html` — slide kelas + demo langkah Linear/Binary.
2. `BBC_Berpikir_Komputasional_Interaktif.html` — belajar CT interaktif (Bahasa Indonesia) + simulasi cari kata + kuis.

**Online (opsional):**
*   VisuAlgo — https://visualgo.net (lihat animasi algoritma)
*   CS Unplugged — https://csunplugged.org (aktivitas tanpa komputer)
*   Bebras Indonesia — https://bebras.or.id (soal teka-teki CT)
*   KBBI Daring — https://kbbi.kemdikbud.go.id (analogi kamus)
*   Inspirasi struktur materi CT: BBC Bitesize  
    https://www.bbc.co.uk/bitesize/guides/zp92mp3/revision/1

---

## 📌 Cheat Sheet (Tempeli di Buku)

| Yang perlu diingat | Versi gampang |
| :--- | :--- |
| Searching | Cari data dengan **aturan** |
| Aturan dulu | Target jelas, samakan huruf, arah cek, kapan stop, hitung cek |
| Linear | Cek **satu-satu** dari depan · data boleh acak |
| Binary | Cek **tengah**, buang setengah · data **wajib terurut** |
| Pilih metode | Belum rapi → Linear · Sudah rapi & banyak → Binary |
| CT | Pecah · cari pola · saring info · susun langkah |

### Satu kalimat penutup
**Linear = telaten dari depan.  
Binary = pintar potong setengah — tapi daftarnya harus rapi dulu.**

Kerjakan `Lembar_Aktivitas_Minggu_2.md` untuk latihan tracing.  
Kalau masih bingung Binary, ulangi dulu game tebak angka 1–100 — idenya sama persis.
