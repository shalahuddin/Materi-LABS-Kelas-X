# Bahan Ajar Detail: Analisis Data

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Alokasi Waktu:** Pendukung Modul 6 (Analisis Data)

---

## 1. Pengenalan Perkakas Analisis Data (Google Sheets / Microsoft Excel)

Perkakas pengolah lembar kerja (*spreadsheet*) seperti Microsoft Excel atau Google Sheets adalah alat yang paling umum digunakan untuk mengolah, menganalisis, dan memvisualisasikan data tanpa perlu keahlian pemrograman khusus.

### A. Konsep Dasar Spreadsheet
*   **Cell (Sel):** Kotak pertemuan antara kolom (diberi nama dengan huruf: A, B, C...) dan baris (diberi nama dengan angka: 1, 2, 3...). Contoh: `B5` berarti sel pada kolom B baris ke-5.
*   **Range (Rentang):** Kumpulan beberapa sel yang dipilih. Contoh: `A1:C10` mencakup seluruh sel dari A1 hingga C10.

### B. Formula Utama Spreadsheet
Di dalam spreadsheet, setiap rumus wajib diawali dengan tanda sama dengan (`=`). Berikut formula yang paling sering digunakan dalam analisis data:

1.  **=SUM(range):** Menghitung total jumlah nilai dalam suatu range.
    *   *Contoh:* `=SUM(C2:C10)` menjumlahkan seluruh nilai dari sel C2 sampai C10.
2.  **=AVERAGE(range):** Menghitung nilai rata-rata dari angka di dalam range.
    *   *Contoh:* `=AVERAGE(D2:D20)` menghitung rata-rata nilai dari D2 sampai D20.
3.  **=COUNT(range):** Menghitung jumlah sel yang berisi angka di dalam range.
    *   *Contoh:* `=COUNT(A2:A50)` menghitung berapa banyak data angka yang ada di kolom A.
4.  **=IF(kondisi; nilai_jika_benar; nilai_jika_salah):** Mengambil keputusan logika berdasarkan kondisi tertentu.
    *   *Contoh:* `=IF(E2>=75; "LULUS"; "REMIDIAL")` mengecek nilai di sel E2. Jika nilainya 75 atau lebih, output-nya "LULUS", jika kurang dari 75, output-nya "REMIDIAL".
5.  **=VLOOKUP(nilai_kunci; range_tabel; indeks_kolom; [terurut]):** Mencari nilai di kolom pertama suatu tabel dan mengembalikan nilai di baris yang sama dari kolom lain yang ditentukan (secara vertikal).
    *   *Contoh:* `=VLOOKUP(A2; G2:I100; 3; FALSE)` mencari kecocokan nilai sel A2 di kolom pertama rentang G2:I100, lalu mengembalikan nilai dari kolom ke-3 pada baris yang cocok.
6.  **=HLOOKUP(nilai_kunci; range_tabel; indeks_baris; [terurut]):** Mirip VLOOKUP, tetapi pencarian dilakukan secara horizontal (mendatar) pada baris pertama tabel.

---

## 2. Koleksi Data (Data Collection)

Koleksi data adalah proses mengumpulkan informasi dari berbagai sumber untuk diolah dan dianalisis guna menjawab suatu permasalahan.

### A. Jenis Sumber Data
1.  **Data Primer:** Data yang diperoleh secara langsung dari sumber pertama/objek penelitian.
    *   *Contoh:* Mengisi kuesioner, hasil wawancara, catatan observasi langsung di lapangan.
2.  **Data Sekunder:** Data yang sudah dikumpulkan oleh pihak lain dan dapat diakses publik.
    *   *Contoh:* Data statistik BPS (Badan Pusat Statistik), artikel berita, jurnal penelitian ilmiah, dataset publik di internet.

### B. Metode Koleksi Data
1.  **Kuesioner/Survei:** Mengumpulkan jawaban dari responden menggunakan daftar pertanyaan terstruktur (menggunakan Google Forms, KoboToolbox, atau kertas).
2.  **Web Scraping (Pengerukan Data Web):** Teknik otomatis menggunakan script program (seperti Python dengan library BeautifulSoup) untuk mengambil data terstruktur dari halaman website publik.
3.  **API (Application Programming Interface):** Mengambil data dari aplikasi lain menggunakan jalur resmi yang disediakan pengembang. Contoh: Mengambil data cuaca dari API OpenWeatherMap.
4.  **Sensus/Observasi:** Mencatat data secara berkala atau menyeluruh terhadap objek yang diamati.

### C. Etika dan Privasi Data
Dalam mengumpulkan data, kita wajib mematuhi etika pengumpulan data:
*   **Informed Consent:** Responden harus tahu tujuan pengumpulan data dan setuju datanya diambil.
*   **Anonimitas:** Menghapus informasi identitas pribadi (seperti nama lengkap, alamat detail, nomor HP) dari dataset agar privasi responden terlindungi (de-identifikasi).
*   **Hak Cipta & Ketentuan Penggunaan:** Tidak mengambil data dari website yang melarang aktivitas pengerukan (*web scraping*).

---

## 3. Visualisasi Data (Data Visualization)

Visualisasi data adalah teknik menyajikan data mentah berupa angka menjadi bentuk grafik atau diagram agar informasi lebih mudah dipahami dan dibaca oleh manusia.

### A. Jenis-Jenis Diagram dan Kapan Harus Digunakan
1.  **Diagram Batang (Bar/Column Chart):**
    *   *Fungsi:* Membandingkan nilai antar-kategori yang berbeda.
    *   *Contoh:* Membandingkan jumlah siswa laki-laki dan perempuan di kelas X-1 s.d. X-5, atau jumlah penjualan produk per bulan.
2.  **Diagram Lingkaran (Pie Chart):**
    *   *Fungsi:* Menunjukkan proporsi atau persentase bagian terhadap keseluruhan (total 100%).
    *   *Karakteristik:* Gunakan hanya jika kategori berjumlah sedikit (maksimal 5-7 kategori) agar mudah dibaca.
    *   *Contoh:* Persentase jenis ekskul yang dipilih oleh siswa kelas X.
3.  **Diagram Garis (Line Chart):**
    *   *Fungsi:* Menunjukkan tren atau perubahan nilai dari waktu ke waktu (data kontinu).
    *   *Contoh:* Grafik fluktuasi suhu udara selama satu minggu, atau perkembangan jumlah pengguna internet di Indonesia dari tahun 2015 s.d. 2025.
4.  **Diagram Pencar (Scatter Plot):**
    *   *Fungsi:* Menunjukkan hubungan (korelasi) antara dua variabel numerik yang berbeda.
    *   *Contoh:* Hubungan antara durasi belajar siswa (jam/hari) dengan nilai ujian matematika mereka.

---

## 🌐 Referensi Website Latihan Siswa

1.  **Google Sheets Training / Microsoft Learn:**
    *   *Fungsi:* Tutorial interaktif dasar penggunaan spreadsheet.
    *   *Tautan:* `support.google.com/docs` atau `learn.microsoft.com`.
2.  **Kaggle (kaggle.com/datasets):**
    *   *Fungsi:* Gudang dataset gratis terbesar di dunia.
    *   *Cara pakai:* Siswa diajak mengunduh dataset sederhana (.csv), misalnya data statistik film, cuaca, atau penjualan, untuk kemudian diimpor ke Excel/Google Sheets dan diolah.
3.  **Satu Data Indonesia (data.go.id):**
    *   *Fungsi:* Portal data terbuka resmi milik Pemerintah Indonesia.
    *   *Cara pakai:* Siswa mengunduh data publik daerah mereka (seperti jumlah sekolah, fasilitas kesehatan) untuk melakukan analisis data kontekstual.
4.  **Chart Expo / Canva Chart Maker:**
    *   *Fungsi:* Latihan membuat berbagai jenis infografis data yang estetis secara online.
5.  **Our World in Data (ourworldindata.org):**
    *   *Fungsi:* Situs web visualisasi data interaktif dunia. Sangat bagus untuk bahan belajar bagaimana membaca diagram garis dan diagram sebar berskala besar mengenai isu global.
