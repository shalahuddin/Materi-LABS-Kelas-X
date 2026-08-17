# Bahan Ajar Detail: Berpikir Komputasional (Computational Thinking)

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Alokasi Waktu:** Pendukung Modul 2 & Modul 7
*   **Metode:** Konseptual, Unplugged, Studi Kasus, Teka-Teki Logika

---

## Deskripsi Singkat
Berpikir Komputasional (BK) adalah metode pemecahan masalah dengan menerapkan prinsip-prinsip ilmu komputer (informatika). BK tidak selalu membutuhkan komputer (dapat diajarkan secara *unplugged*). Dokumen ini berisi materi mendalam mengenai penerapan 4 pilar BK untuk mempelajari topik **Pencarian (Searching)**, **Logika Dasar**, **Pengurutan (Sorting)**, serta **Tumpukan (Stack) & Antrean (Queue)** yang disesuaikan untuk siswa SMA Kelas X.

---

## 1. Pencarian (Searching)

### A. Definisi
Pencarian adalah proses menemukan anggota (data/elemen) dari sekumpulan data yang memiliki karakteristik tertentu. Di kehidupan sehari-hari, kita mencari kontak di HP, mencari kata di kamus, atau mencari buku di perpustakaan.

### B. Algoritma Pencarian Standar
Terdapat dua metode pencarian yang paling sering digunakan:
1.  **Pencarian Berurutan (Linear/Sequential Search):**
    *   **Cara kerja:** Memeriksa setiap elemen data satu per satu, mulai dari elemen pertama hingga elemen yang dicari ditemukan atau seluruh data selesai diperiksa.
    *   **Karakteristik:** Dapat digunakan pada kumpulan data yang **acak/belum terurut**.
    *   **Analogi:** Mencari kunci rumah di dalam kotak yang berisi puluhan kunci acak. Anda harus mengambil kunci satu per satu sampai menemukan yang cocok.
2.  **Pencarian Biner (Binary Search):**
    *   **Cara kerja:** Membagi data menjadi dua bagian secara berulang. Algoritma ini membandingkan data yang dicari dengan elemen tengah. Jika sama, data ditemukan. Jika data yang dicari lebih kecil dari nilai tengah, pencarian dilanjutkan ke belahan kiri. Jika lebih besar, pencarian dilanjutkan ke belahan kanan.
    *   **Karakteristik:** **Hanya bisa digunakan** jika kumpulan data **sudah dalam keadaan terurut** (ascending/descending).
    *   **Analogi:** Mencari kata "Informatika" di Kamus Besar Bahasa Indonesia (KBBI). Anda tidak membuka kamus halaman demi halaman dari awal (linear), melainkan langsung membuka bagian tengah, lalu memotong pencarian ke kiri atau kanan berdasarkan urutan abjad.

### C. Aktivitas Kelas (Unplugged): "Tebak Angka Misterius"
*   **Petunjuk:** Guru memikirkan sebuah angka antara 1 sampai 100. Siswa harus menebak angka tersebut.
*   **Aturan:** Guru hanya akan menjawab "Terlalu kecil", "Terlalu besar", atau "Benar".
*   **Simulasi:**
    *   Jika siswa menebak secara acak atau urut 1, 2, 3, ... (Linear Search), tebakan bisa memakan waktu hingga 100 kali.
    *   Jika siswa menerapkan Binary Search, mereka akan menebak angka tengah yaitu **50**. Jika guru menjawab "Terlalu kecil", siswa mengeliminasi angka 1-50, lalu menebak tengah dari 51-100 yaitu **75**, dan seterusnya. Dengan cara ini, angka pasti ditemukan maksimal dalam **7 tebakan** ($2^7 = 128$).

---

## 2. Aktivitas Logika (Logical Thinking)

Berpikir logis membantu komputer mengambil keputusan melalui evaluasi kondisi benar (*True*) atau salah (*False*).

### A. Operator Logika Dasar (Gerbang Logika)
1.  **AND (Dan):** Menghasilkan *True* hanya jika **semua** kondisi bernilai *True*.
    *   *Contoh:* Siswa boleh ikut ujian jika **sudah membayar SPP** AND **kehadiran > 75%**.
2.  **OR (Atau):** Menghasilkan *True* jika **salah satu atau semua** kondisi bernilai *True*.
    *   *Contoh:* Siswa mendapat diskon jika **memiliki kartu OSIS** OR **berulang tahun hari ini**.
3.  **NOT (Negasi/Bukan):** Membalikkan nilai logika. Jika input *True*, hasilnya *False*, dan sebaliknya.
    *   *Contoh:* NOT **Hujan** berarti cuaca sedang cerah/tidak hujan.

### B. Tabel Kebenaran (Truth Table)

| Input A | Input B | A AND B | A OR B | NOT A |
| :---: | :---: | :---: | :---: | :---: |
| False | False | False | False | True |
| False | True | False | True | True |
| True | False | False | True | False |
| True | True | True | True | False |

### C. Latihan Aktivitas Logika: "Logic Grid Puzzle"
*   **Studi Kasus:** Tiga siswa bernama Adi, Budi, dan Cici memakai baju dengan warna berbeda (Merah, Biru, Hijau). Mereka menyukai mata pelajaran yang berbeda (Matematika, IPA, Bahasa Inggris).
*   **Petunjuk:**
    1. Adi tidak memakai baju merah dan tidak suka Matematika.
    2. Siswa yang memakai baju hijau sangat menyukai Bahasa Inggris.
    3. Budi memakai baju biru.
*   **Tantangan:** Tentukan warna baju dan pelajaran favorit masing-masing siswa!
*   **Solusi Tracing (Abstraksi & Pengenalan Pola):**
    *   Dari petunjuk 3: Budi memakai baju **Biru**.
    *   Dari petunjuk 1: Adi tidak memakai baju merah. Karena Budi memakai Biru, maka Adi harus memakai baju **Hijau**. Sisa baju **Merah** dipakai oleh Cici.
    *   Dari petunjuk 2: Siswa berbaju hijau suka Bahasa Inggris. Karena Adi berbaju hijau, maka Adi suka **Bahasa Inggris**.
    *   Dari petunjuk 1: Adi tidak suka Matematika. Budi juga tersisa pilihan Matematika atau IPA. Karena Adi sudah menyukai Bahasa Inggris, kita analisis Budi dan Cici. Jika Cici berbaju merah, dan Adi tidak suka Matematika, berarti pelajaran Matematika dan IPA dibagi antara Budi dan Cici. Melalui analisis deduksi, kita dapat memetakan kecocokan penuh secara sistematis.

---

## 3. Pengurutan (Sorting)

Pengurutan adalah proses menyusun elemen-elemen data berdasarkan aturan tertentu (dari terkecil ke terbesar / *Ascending*, atau terbesar ke terkecil / *Descending*).

### A. Algoritma Pengurutan Dasar (Untuk Semester Ganjil)
1.  **Bubble Sort (Pengurutan Gelembung):**
    *   **Cara kerja:** Membandingkan dua data yang bersebelahan secara berulang, lalu menukarnya jika urutannya salah. Data terbesar akan "mengapung" ke posisi akhir seperti gelembung sabun.
    *   **Karakteristik:** Sangat lambat untuk data besar, tetapi sangat sederhana dipahami.
2.  **Selection Sort (Pengurutan Pilihan):**
    *   **Cara kerja:** Mencari nilai terkecil dari seluruh data yang belum terurut, lalu menukarnya dengan data di posisi pertama. Langkah ini diulangi untuk posisi berikutnya.
    *   **Karakteristik:** Jumlah pertukaran data (*swap*) minimal.
3.  **Insertion Sort (Pengurutan Penyisipan):**
    *   **Cara kerja:** Mengambil satu per satu data dan menyisipkannya ke posisi yang tepat pada bagian data yang sudah terurut.
    *   **Karakteristik:** Sangat efisien untuk data yang hampir terurut. Mirip cara manusia mengurutkan kartu di tangan.

### B. Algoritma Pengurutan Lanjutan (Untuk Semester Genap)
1.  **Merge Sort (Pengurutan Gabung):**
    *   **Cara kerja:** Menggunakan metode *Divide and Conquer* (Bagi dan Atasi). Membagi data menjadi sub-bagian terkecil (berisi 1 elemen), lalu menggabungkannya kembali secara terurut.
2.  **Quick Sort (Pengurutan Cepat):**
    *   **Cara kerja:** Memilih satu elemen sebagai pivot, lalu mempartisi elemen lain menjadi dua kelompok: yang lebih kecil dari pivot (di sebelah kiri) dan yang lebih besar dari pivot (di sebelah kanan), kemudian mengulangi proses secara rekursif.

---

## 4. Tumpukan (Stack) dan Antrean (Queue)

Ini adalah dua konsep struktur data linier yang mengatur bagaimana elemen data disimpan dan diambil.

### A. Tumpukan (Stack - LIFO: Last In First Out)
*   **Konsep:** Elemen yang **terakhir dimasukkan** adalah elemen yang **pertama kali dikeluarkan**.
*   **Analogi Nyata:**
    *   Tumpukan piring di dapur: Anda hanya bisa mengambil piring paling atas yang baru ditaruh.
    *   Fitur tombol *Undo* (Ctrl+Z) di komputer: Aksi terakhir yang Anda lakukan adalah yang pertama kali dibatalkan.
    *   Tombol *Back* di browser internet.
*   **Operasi Dasar:**
    *   `Push`: Memasukkan data ke atas tumpukan.
    *   `Pop`: Mengambil data teratas dari tumpukan.

### B. Antrean (Queue - FIFO: First In First Out)
*   **Konsep:** Elemen yang **pertama kali masuk** adalah elemen yang **pertama kali keluar**.
*   **Analogi Nyata:**
    *   Antrean pembeli di kasir: Orang pertama yang mengantre akan dilayani terlebih dahulu.
    *   Antrean cetak dokumen di printer (*print spooler*).
    *   Mobil melewati loket pembayaran tol.
*   **Operasi Dasar:**
    *   `Enqueue`: Memasukkan data ke barisan belakang antrean.
    *   `Dequeue`: Mengambil/mengeluarkan data dari barisan depan antrean.

---

## 🌐 Referensi Website Interaktif untuk Latihan Siswa

Gunakan situs web berikut untuk melatih kemampuan berpikir komputasional di kelas atau sebagai tugas mandiri:

1.  **Tantangan Bebras (bebras.or.id / bebras.org):**
    *   *Fungsi:* Latihan soal logika berpikir komputasional tingkat dunia (SD, SMP, SMA).
    *   *Cara pakai:* Guru memberikan contoh soal "Tantangan Bebras" tingkat SMA (Fase E/Siber) untuk melatih dekomposisi dan pola.
2.  **VisuAlgo (visualgo.net):**
    *   *Fungsi:* Visualisasi animasi interaktif jalannya algoritma secara real-time.
    *   *Cara pakai:* Buka menu **Sorting** atau **BSTS/Graphs** untuk mendemonstrasikan secara visual bagaimana Bubble/Selection/Merge Sort memindahkan data, serta bagaimana Stack dan Queue bekerja.
3.  **CS Unplugged (csunplugged.org):**
    *   *Fungsi:* Menyediakan modul game fisik tanpa komputer untuk mengajarkan konsep Searching, Sorting, dan Binary.
4.  **Blockly Games (blockly.games):**
    *   *Fungsi:* Game pemrograman berbasis blok visual yang melatih logika perulangan, percabangan, dan penyelesaian masalah.
5.  **Flowgorithm (flowgorithm.org):**
    *   *Fungsi:* Aplikasi gratis untuk menggambar flowchart dan menjalankannya secara interaktif guna memahami alur logika program secara langsung.
