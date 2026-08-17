# Lembar Aktivitas Siswa Minggu 3: Searching via Pseudocode

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Semester:** Ganjil - Minggu 3
*   **Modul:** Modul 2 — Berpikir Komputasional (Pseudocode)
*   **Materi:** Pseudocode + Searching (Linear & Binary)
*   **Mode Pengerjaan:** **INDIVIDU** (diskusi boleh, jawaban tetap sendiri)
*   **Nama Siswa:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
*   **No. Absen / Kelas:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## 🎯 Tujuan Tugas
1. Melengkapi dan menulis pseudocode **Linear Search** dengan benar.
2. Melengkapi dan menulis pseudocode **Binary Search** dengan benar.
3. Men-trace (menelusuri) pseudocode dan menghitung jumlah perbandingan.
4. Memilih metode pencarian yang tepat beserta alasannya.

**Total skor: 100 poin** (5 soal × 20 poin)

---

## ✏️ Soal 1: Lengkapi Pseudocode Linear Search (20 poin)

Lengkapi bagian yang kosong (bisa lebih dari 1 kata):

```text
ALGORITMA CariLinear(daftar[], target)
  UNTUK i = 0 SAMPAI ________ - 1
    JIKA daftar[i] ________ target MAKA
      KEMBALIKAN ________
    SELESAI JIKA
  SELESAI UNTUK
  KEMBALIKAN ________
SELESAI ALGORITMA
```

*   Blank 1 (`SAMPAI ... - 1`) berisi: \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 2 (`daftar[i] ... target`) berisi operator: \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 3 (nilai yang dikembalikan saat ketemu): \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 4 (nilai yang dikembalikan jika tidak ketemu): \_\_\_\_\_\_\_\_\_\_\_\_

**Pertanyaan singkat:** Mengapa perulangan berhenti di `panjang(daftar) - 1`, bukan di `panjang(daftar)`?

> Jawaban: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## ✏️ Soal 2: Lengkapi Pseudocode Binary Search (20 poin)

```text
ALGORITMA CariBinary(daftar_terurut[], target)
  kiri  ← 0
  kanan ← ________
  SELAMA kiri ________ kanan
    tengah ← (kiri + kanan) / 2
    JIKA daftar_terurut[tengah] == target MAKA
      KEMBALIKAN ________
    LAINNYA JIKA daftar_terurut[tengah] < target MAKA
      kiri  ← ________
    LAINNYA
      kanan ← ________
    SELESAI JIKA
  SELESAI SELAMA
  KEMBALIKAN ________
SELESAI ALGORITMA
```

*   Blank 1 (nilai awal `kanan`): \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 2 (kondisi `SELAMA`): \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 3 (nilai dikembalikan saat ketemu): \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 4 (nilai baru `kiri`): \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 5 (nilai baru `kanan`): \_\_\_\_\_\_\_\_\_\_\_\_
*   Blank 6 (nilai jika tidak ketemu): \_\_\_\_\_\_\_\_\_\_\_\_

**Pertanyaan singkat:** Syarat apa yang WAJIB dipenuhi sebelum Binary Search dipakai?

> Jawaban: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## ✏️ Soal 3: Trace Linear Search (20 poin)

Gunakan pseudocode Linear Search. Data (**tidak diurutkan**):

| Index | 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Kata | KAMERA | MEJA | BUKU | LAMPU | TAS |

### Target: `TAS`
| Langkah | Index dicek | Kata | Cocok? (Y/T) |
| :-: | :-: | :--- | :-: |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

*   Hasil: **[ Ketemu di index ____ / Tidak ditemukan ]**
*   Jumlah perbandingan: **____**

### Target: `PULPEN` (sengaja tidak ada)
*   Jumlah perbandingan sampai selesai: **____**
*   Kesimpulan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## ✏️ Soal 4: Trace Binary Search (20 poin)

Gunakan pseudocode Binary Search. Data **sudah A–Z**:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Kata | BUKU | KAMERA | KURSI | LAMPU | MEJA | MOUSE | TAS |

### Target: `MOUSE`
| Iterasi | kiri | kanan | tengah | daftar[tengah] | Keputusan (ketemu / ke kiri / ke kanan) |
| :-: | :-: | :-: | :-: | :--- | :--- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

*   Hasil akhir: index **____**
*   Jumlah perbandingan: **____**

### Target: `TAS`
*   Index ketemu: **____**
*   Jumlah perbandingan: **____**

---

## ✏️ Soal 5: Menulis Pseudocode dari Skenario (20 poin)

Tulis **pseudocode lengkap** (pakai `MULAI` ... `SELESAI`) untuk setiap skenario berikut:

### A. Cek Kehadiran (10 poin)
Kelasmu punya daftar absensi berisi 30 nama (**belum urut**). Tulis pseudocode untuk mencari apakah nama **"Raka"** ada di daftar itu, lalu menampilkan pesan "HADIR" atau "TIDAK HADIR".

```text

```

*(Tulis jawabanmu di kotak di atas)*

### B. Cari Kata di KBBI Mini (10 poin)
Kamu punya 200 kata **sudah urut A–Z**. Tulis pseudocode untuk mencari kata **"SEARCH"** secepat mungkin.

```text

```

*(Tulis jawabanmu di kotak di atas)*

---

## 📝 Penilaian Mandiri (Self Assessment)

*Skor: **3** Sangat Baik · **2** Cukup · **1** Perlu ditingkatkan*

| Aspek | Skor (1–3) | Catatan |
| :--- | :-: | :--- |
| Saya memahami cara menulis pseudocode | | |
| Saya bisa menulis pseudocode Linear Search | | |
| Saya bisa menulis pseudocode Binary Search | | |
| Saya bisa men-trace pseudocode searching | | |
| Saya bisa memilih metode dengan alasan | | |
| Saya mengerjakan sendiri & tepat waktu | | |

---

## 🏆 Pengayaan (Opsional)
1. Bandingkan jumlah perbandingan Linear vs Binary pada data 30 item terurut untuk target yang sama — catat hasilnya.
2. Ubah pseudocode Binary Search-mu agar bekerja untuk data angka (bukan kata).
3. Tantangan: tulis pseudocode untuk mencari nilai **terbesar** dalam sebuah daftar.

---

**Tanda Tangan Siswa:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | **Tanda Tangan Guru:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | **Tanggal:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Rubrik Cepat Guru

| Kriteria | A (85–100) | B (70–84) | C (<70) |
| :--- | :--- | :--- | :--- |
| Melengkapi pseudocode | Benar semua blank | 1–2 blank salah | Banyak blank salah |
| Men-trace Linear | Benar semua langkah | 1 kesalahan kecil | Konsep belum pas |
| Men-trace Binary | kiri/mid/kanan benar | Sedikit salah hitung | Konsep belum pas |
| Menulis pseudocode sendiri | Struktur & aturan tepat | Struktur hampir tepat | Belum sesuai aturan |
| Kemandirian | Mandiri, rapi | Sedikit dibantu | Tidak lengkap |
