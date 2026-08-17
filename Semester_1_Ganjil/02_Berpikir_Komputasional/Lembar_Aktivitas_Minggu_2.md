# Lembar Aktivitas Siswa: Aturan Mencari Kata (Searching)

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Semester:** Ganjil - Minggu 2
*   **Modul:** Modul 2 — Berpikir Komputasional (Searching)
*   **Mode Pengerjaan:** **INDIVIDU** (simulasi boleh berpasangan, jawaban tetap sendiri)
*   **Nama Siswa:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
*   **No. Absen / Kelas:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## 🎯 Tujuan Aktivitas
1. Menyusun **aturan mencari kata** yang jelas dan konsisten.
2. Menerapkan **Linear Search** pada data acak dan mencatat jumlah perbandingan.
3. Menerapkan **Binary Search** pada data terurut dan menjelaskan syaratnya.
4. Memilih metode pencarian yang tepat dengan alasan.

---

## 🧩 Aktivitas 1 (Pertemuan 1): Aturan + Linear Search

### A. Aturan Mencari Kata (isi sendiri)
Lengkapi aturan main sebelum mencari:

| No | Aspek Aturan | Jawaban Saya |
| :-: | :--- | :--- |
| 1 | Target yang saya cari (tulis 1 kata) | |
| 2 | Apakah huruf besar/kecil diseragamkan? (Ya/Tidak + contoh) | |
| 3 | Kriteria "ketemu" (sama persis / boleh mirip?) | |
| 4 | Kapan pencarian berhenti? | |
| 5 | Apa yang dilaporkan jika tidak ketemu? | |

**Hubungkan ke CT (centang yang kamu pakai):**  
[ ] Dekomposisi   [ ] Pengenalan Pola   [ ] Abstraksi   [ ] Algoritma  

Jelaskan singkat 1 pilar yang paling terasa:
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### B. Linear Search — Daftar Acak
Gunakan daftar berikut (**jangan diurutkan**):

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Kata | MEJA | BUKU | LAMPU | TAS | PENSIL | KOMPUTER | PENGHAPUS | KURSI | MOUSE | KAMERA |

#### Target 1: `PENSIL`
| Langkah | Index dicek | Kata | Cocok? (Y/T) |
| :-: | :-: | :--- | :-: |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

*   Hasil: **[ Ketemu di index ____ / Tidak ditemukan ]**
*   Jumlah perbandingan: **____**

#### Target 2: `KAMERA`
*   Index ketemu: **____** (atau tidak ditemukan)
*   Jumlah perbandingan: **____**
*   Termasuk kasus: **[ Terbaik / Rata-rata / Terburuk ]** — alasan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### Target 3: `PRINTER` (sengaja tidak ada di daftar)
*   Jumlah perbandingan sampai selesai: **____**
*   Kesimpulan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### C. Pseudocode Linear (lengkapi bagian kosong)
```
ALGORITMA LinearSearchKata(daftar[], target)
  FOR i = 0 TO ________ DO
    IF daftar[i] == ________ THEN
      RETURN ________
    END IF
  END FOR
  RETURN ________
END ALGORITMA
```

### D. Refleksi Pertemuan 1
1. Kelebihan Linear Search: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2. Kelemahan Linear Search: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. Satu hal yang saya pelajari hari ini: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## 💻 Aktivitas 2 (Pertemuan 2): Binary Search + Perbandingan

### A. Syarat Binary Search
Jawablah:
1. Binary Search **hanya** boleh dipakai jika data: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2. Jika data acak lalu dipaksa Binary, risiko yang terjadi: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### B. Binary Search — Kamus Mini (sudah A–Z)
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Kata | ALGORITMA | BINARY | DATA | FILE | INPUT | KOMPUTER | LOGIKA | MOUSE | OUTPUT | PROGRAM | QUEUE | SEARCH | STACK | VARIABEL | WEB |

#### Target 1: `PROGRAM`
Isi jejak tiap iterasi:

| Iterasi | left | right | mid | daftar[mid] | Keputusan (ketemu / ke kiri / ke kanan) |
| :-: | :-: | :-: | :-: | :--- | :--- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

*   Hasil akhir: index **____**
*   Jumlah perbandingan: **____**

#### Target 2: `BINARY`
*   Index ketemu: **____**
*   Jumlah perbandingan: **____**

#### Target 3: `PYTHON` (tidak ada)
*   Iterasi terakhir left=____ right=____ → kesimpulan: **Tidak ditemukan**
*   Jumlah perbandingan: **____**

### C. Bandingkan Metode (target yang sama)

Ambil target **`SEARCH`** pada kamus mini:

| Metode | Cara menghitung | Jumlah perbandingan |
| :--- | :--- | :-: |
| Linear Search | Cek dari index 0 ke kanan sampai ketemu SEARCH | |
| Binary Search | Pakai left–mid–right pada kamus mini | |

**Pertanyaan:**
1. Mana yang lebih sedikit langkah untuk data terurut berukuran sedang/besar? **[ Linear / Binary ]**
2. Jika daftar hanya 4 kata dan acak, metode yang lebih praktis? **[ Linear / Binary ]** — alasan: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### D. Soal Pilih Metode (beri alasan 1 kalimat)

| No | Situasi | Pilih (L/B) | Alasan |
| :-: | :--- | :-: | :--- |
| 1 | Mencari pulpen di kotak alat tulis campur aduk | | |
| 2 | Mencari kata "INFORMATIKA" di KBBI cetak | | |
| 3 | Mencari nama di absensi yang belum diurutkan | | |
| 4 | Mencari nomor halaman 128 di buku 300 hlm | | |
| 5 | Mencari 1 file di folder berisi 5 file acak | | |

### E. Pseudocode Binary (lengkapi)
```
ALGORITMA BinarySearchKata(daftar_terurut[], target)
  left  ← 0
  right ← ________
  WHILE left ____ right DO
    mid ← (left + right) DIV 2
    IF daftar_terurut[mid] == target THEN
      RETURN mid
    ELSE IF daftar_terurut[mid] < target THEN
      left ← ________
    ELSE
      right ← ________
    END IF
  END WHILE
  RETURN -1
END ALGORITMA
```

---

## 📝 Penilaian Mandiri (Self Assessment)

*Skor: **3** Sangat Baik · **2** Cukup · **1** Perlu ditingkatkan*

| Aspek | Skor (1–3) | Catatan |
| :--- | :-: | :--- |
| Saya memahami aturan mencari kata | | |
| Saya bisa men-trace Linear Search | | |
| Saya paham Binary wajib data terurut | | |
| Saya bisa men-trace Binary Search | | |
| Saya bisa memilih metode dengan alasan | | |
| Saya mengerjakan sendiri & tepat waktu | | |

### Refleksi Akhir Minggu 2
1. Satu ide CT yang paling nempel minggu ini:  
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2. Di kehidupan nyata, saya akan pakai cara Binary saat:  
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. Yang masih membingungkan:  
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## 🏆 Pengayaan (Opsional)
1. Buka visualisasi searching (VisuAlgo atau video Binary Search).
2. Tulis 3 perbedaan yang kamu lihat antara animasi Linear dan Binary.
3. Tantangan Bebras: kerjakan 1 soal yang melibatkan strategi pencarian/efisiensi; sebutkan pilar CT yang dipakai.

---

**Tanda Tangan Siswa:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | **Tanda Tangan Guru:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_ | **Tanggal:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Rubrik Cepat Guru

| Kriteria | A (85–100) | B (70–84) | C (<70) |
| :--- | :--- | :--- | :--- |
| Aturan mencari kata | Lengkap & konsisten | Hampir lengkap | Samar |
| Tracing Linear | Benar semua target | 1 kesalahan kecil | Banyak salah |
| Tracing Binary | left/mid/right benar | Sedikit salah hitung | Konsep belum pas |
| Pilih metode | Alasan tepat | Alasan dangkal | Salah pilih |
| Kemandirian | Mandiri, rapi | Sedikit dibantu | Tidak lengkap |
