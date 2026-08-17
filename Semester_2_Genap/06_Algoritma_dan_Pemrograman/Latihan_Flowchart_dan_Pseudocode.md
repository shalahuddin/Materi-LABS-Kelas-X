# Buku Kerja Praktik: Latihan Flowchart, Pseudocode, dan Pemrograman Python

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Alokasi Waktu:** Pendukung Modul 7 (Algoritma dan Pemrograman)

---

## 1. Panduan Singkat Penulisan Algoritma

Algoritma adalah urutan langkah logis yang digunakan untuk memecahkan suatu masalah. Algoritma dapat disajikan dalam bentuk bahasa alami (deskriptif), diagram alur (**Flowchart**), atau kode semu (**Pseudocode**).

### A. Simbol Standar Flowchart (Standar ISO)

| Simbol | Nama | Fungsi |
| :---: | :---: | :--- |
| `[ Oval / Capsul ]` | **Terminator** | Menandakan awal (`Mulai` / `Start`) atau akhir (`Selesai` / `End`) dari program. |
| `[ Jajar Genjang ]` | **Input / Output** | Menandakan proses membaca data dari pengguna (`Input`) atau menampilkan hasil (`Output`). |
| `[ Persegi Panjang ]` | **Process (Proses)** | Menandakan perhitungan matematika, inisialisasi variabel, atau manipulasi data internal. |
| `[ Belah Ketupat ]` | **Decision (Keputusan)** | Menunjukkan percabangan kondisi (Ya/Tidak). Digunakan untuk logika percabangan. |
| `[ Panah (Lines) ]` | **Flow Line** | Menunjukkan arah aliran eksekusi program. |

### B. Aturan Penulisan Pseudocode
Pseudocode adalah deskripsi algoritma pemrograman yang menggunakan konvensi struktural dari bahasa pemrograman komputer, tetapi ditujukan agar mudah dibaca oleh manusia.
*   Gunakan kata kunci standar seperti: `INPUT`, `READ`, `OUTPUT`, `WRITE`, `PRINT`, `IF...THEN...ELSE`, `FOR...TO...DO`, `WHILE...DO`.
*   Tuliskan nama variabel dengan jelas (misal: `alas`, `tinggi`, `luas`).
*   Gunakan indentasi (jorokan ke dalam) untuk blok percabangan dan perulangan.

---

## 2. Kumpulan Studi Kasus & Latihan Bertingkat

---

### 💡 LEVEL 1: STRUKTUR SEKUENSIAL (Berurutan Tanpa Cabang/Loop)

#### Kasus 1: Menghitung Luas Segitiga
*   **Deskripsi Masalah:** Buatlah algoritma untuk menghitung luas segitiga berdasarkan input alas dan tinggi dari pengguna.
*   **Prinsip Berpikir Komputasional:**
    *   *Dekomposisi:* Membagi masalah menjadi input (alas, tinggi), proses (rumus luas = 0.5 * alas * tinggi), dan output (luas).
    *   *Abstraksi:* Mengabaikan satuan fisik (cm, m) dan fokus pada nilai angka.
*   **Pseudocode:**
    ```text
    PROGRAM HitungLuasSegitiga
    DEKLARASI
        alas, tinggi, luas : REAL
    ALGORITMA:
        INPUT alas
        INPUT tinggi
        luas <- 0.5 * alas * tinggi
        OUTPUT luas
    ```
*   **Flowchart (ASCII):**
    ```text
         ( Mulai )
             |
       [ Input alas ]
             |
      [ Input tinggi ]
             |
     [ luas = 0.5 * alas * tinggi ]
             |
       [ Output luas ]
             |
        ( Selesai )
    ```
*   **Kode Python:**
    ```python
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga adalah:", luas)
    ```

---

#### Kasus 2: Konversi Suhu Celcius ke Fahrenheit
*   **Deskripsi Masalah:** Konversikan suhu dalam Celcius ($C$) ke skala Fahrenheit ($F$) menggunakan rumus: $F = (9/5 \times C) + 32$.
*   **Pseudocode:**
    ```text
    PROGRAM KonversiSuhu
    DEKLARASI
        celsius, fahrenheit : REAL
    ALGORITMA:
        INPUT celsius
        fahrenheit <- (9.0 / 5.0 * celsius) + 32
        OUTPUT fahrenheit
    ```
*   **Flowchart (ASCII):**
    ```text
         ( Mulai )
             |
      [ Input celsius ]
             |
     [ fahrenheit = (9/5 * celsius) + 32 ]
             |
     [ Output fahrenheit ]
             |
        ( Selesai )
    ```
*   **Kode Python:**
    ```python
    celsius = float(input("Masukkan suhu Celcius: "))
    fahrenheit = (9/5 * celsius) + 32
    print("Suhu dalam Fahrenheit adalah:", fahrenheit)
    ```

---

### 💡 LEVEL 2: STRUKTUR PERCABANGAN (Kondisional / IF-ELSE)

#### Kasus 3: Menentukan Bilangan Ganjil atau Genap
*   **Deskripsi Masalah:** Pengguna memasukkan sebuah bilangan bulat. Tentukan apakah bilangan tersebut genap atau ganjil.
*   **Pseudocode:**
    ```text
    PROGRAM GanjilGenap
    DEKLARASI
        angka : INTEGER
    ALGORITMA:
        INPUT angka
        IF angka MOD 2 = 0 THEN
            OUTPUT "Bilangan Genap"
        ELSE
            OUTPUT "Bilangan Ganjil"
        ENDIF
    ```
*   **Flowchart (ASCII):**
    ```text
              ( Mulai )
                  |
            [ Input angka ]
                  |
          / Apakah angka \
         <   MOD 2 = 0    >
          \              /
            /          \
        (Ya)            (Tidak)
       /                  \
[ Output "Genap" ]   [ Output "Ganjil" ]
       \                  /
            \        /
            ( Selesai )
    ```
*   **Kode Python:**
    ```python
    angka = int(input("Masukkan bilangan bulat: "))
    if angka % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")
    ```

---

#### Kasus 4: Menentukan Kelulusan Siswa (KKM)
*   **Deskripsi Masalah:** Siswa dinyatakan lulus jika nilai ujian $\ge 75$. Jika kurang, dinyatakan tidak lulus.
*   **Kode Python:**
    ```python
    nilai = float(input("Masukkan nilai ujian: "))
    if nilai >= 75:
        print("LULUS")
    else:
        print("TIDAK LULUS")
    ```

---

#### Kasus 5: Klasifikasi Nilai Huruf (Multi-Kondisi)
*   **Deskripsi Masalah:** Konversi nilai angka ($0-100$) menjadi nilai huruf ($A, B, C, D, E$):
    *   $\ge 90$: A
    *   $\ge 80$ dan $< 90$: B
    *   $\ge 70$ dan $< 80$: C
    *   $\ge 60$ dan $< 70$: D
    *   $< 60$: E
*   **Pseudocode:**
    ```text
    PROGRAM KlasifikasiNilai
    DEKLARASI
        nilai : REAL
    ALGORITMA:
        INPUT nilai
        IF nilai >= 90 THEN
            OUTPUT "A"
        ELSE IF nilai >= 80 THEN
            OUTPUT "B"
        ELSE IF nilai >= 70 THEN
            OUTPUT "C"
        ELSE IF nilai >= 60 THEN
            OUTPUT "D"
        ELSE
            OUTPUT "E"
        ENDIF
    ```
*   **Kode Python:**
    ```python
    nilai = float(input("Masukkan nilai angka: "))
    if nilai >= 90:
        print("A")
    elif nilai >= 80:
        print("B")
    elif nilai >= 70:
        print("C")
    elif nilai >= 60:
        print("D")
    else:
        print("E")
    ```

---

### 💡 LEVEL 3: STRUKTUR PERULANGAN (Looping / FOR & WHILE)

#### Kasus 6: Mencetak Angka 1 sampai N
*   **Deskripsi Masalah:** Menerima input bilangan bulat positif $N$. Cetak semua angka dari 1 sampai $N$.
*   **Pseudocode:**
    ```text
    PROGRAM CetakAngka
    DEKLARASI
        n, i : INTEGER
    ALGORITMA:
        INPUT n
        FOR i <- 1 TO n DO
            OUTPUT i
        ENDFOR
    ```
*   **Flowchart (ASCII):**
    ```text
              ( Mulai )
                  |
             [ Input n ]
                  |
             [  i = 1  ]
                  |
           /  Apakah i   \
          <   <= n        >
           \             /
             /         \
         (Ya)           (Tidak)
        /                 \
   [ Output i ]            |
       |                   |
  [ i = i + 1 ]            |
       |                   |
       \___________________/
                           |
                      ( Selesai )
    ```
*   **Kode Python:**
    ```python
    n = int(input("Masukkan batas angka N: "))
    for i in range(1, n + 1):
        print(i)
    ```

---

#### Kasus 7: Menghitung Jumlah Deret Angka ($1 + 2 + \dots + N$)
*   **Deskripsi Masalah:** Hitung total penjumlahan angka dari 1 sampai $N$. Contoh jika $N=4$, hasilnya $10$ ($1+2+3+4$).
*   **Kode Python:**
    ```python
    n = int(input("Masukkan nilai N: "))
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print("Total penjumlahan deret adalah:", total)
    ```

---

#### Kasus 8: Tebak Angka dengan Batasan (Perulangan Kondisional)
*   **Deskripsi Masalah:** Program memiliki angka rahasia = 7. Pengguna terus diminta menebak angka sampai tebakannya benar.
*   **Pseudocode:**
    ```text
    PROGRAM TebakAngka
    DEKLARASI
        angka_rahasia, tebakan : INTEGER
    ALGORITMA:
        angka_rahasia <- 7
        tebakan <- 0
        WHILE tebakan != angka_rahasia DO
            INPUT tebakan
            IF tebakan != angka_rahasia THEN
                OUTPUT "Tebakan Anda salah, coba lagi!"
            ENDIF
        ENDWHILE
        OUTPUT "Selamat! Tebakan Anda benar."
    ```
*   **Kode Python:**
    ```python
    angka_rahasia = 7
    tebakan = 0
    while tebakan != angka_rahasia:
        tebakan = int(input("Tebak angka rahasia (1-10): "))
        if tebakan != angka_rahasia:
            print("Salah! Coba lagi.")
    print("Selamat! Tebakan Anda benar.")
    ```

---

### 💡 LEVEL 4: KASUS INTEGRATIF (Kombinasi Looping, Percabangan & Struktur Data)

#### Kasus 9: Mencari Nilai Maksimum dari Kumpulan Angka (Linear Search Concept)
*   **Deskripsi Masalah:** Cari nilai terbesar dari $5$ angka yang dimasukkan pengguna secara berturut-turut.
*   **Pseudocode:**
    ```text
    PROGRAM CariMaksimum
    DEKLARASI
        i, angka, max_nilai : INTEGER
    ALGORITMA:
        INPUT angka
        max_nilai <- angka
        FOR i <- 2 TO 5 DO
            INPUT angka
            IF angka > max_nilai THEN
                max_nilai <- angka
            ENDIF
        ENDFOR
        OUTPUT max_nilai
    ```
*   **Kode Python:**
    ```python
    max_nilai = int(input("Masukkan angka ke-1: "))
    for i in range(2, 6):
        angka = int(input(f"Masukkan angka ke-{i}: "))
        if angka > max_nilai:
            max_nilai = angka
    print("Angka terbesar adalah:", max_nilai)
    ```

---

#### Kasus 10: Kasir Sederhana Toko Buku (Kombinasi Multi-Elemen)
*   **Deskripsi Masalah:** Hitung total belanja buku. Pengguna memasukkan harga buku dan jumlah beli. Berikan diskon 10% jika total belanja melebihi Rp 100.000.
*   **Kode Python:**
    ```python
    harga = float(input("Masukkan harga buku (Rp): "))
    jumlah = int(input("Masukkan jumlah buku yang dibeli: "))
    
    total_kotor = harga * jumlah
    
    if total_kotor > 100000:
        diskon = 0.1 * total_kotor
        total_akhir = total_kotor - diskon
        print("Selamat! Anda mendapat diskon 10%")
    else:
        diskon = 0
        total_akhir = total_kotor
        
    print("Total kotor : Rp", total_kotor)
    print("Diskon      : Rp", diskon)
    print("Total Bayar : Rp", total_akhir)
    ```

---

## 🌐 Referensi Website Latihan Siswa

1.  **Flowgorithm (flowgorithm.org):**
    *   *Fungsi:* Aplikasi visual interaktif terbaik untuk membuat dan menjalankan flowchart langsung tanpa koding manual. Dapat mengonversi flowchart ke bahasa Python secara otomatis.
2.  **Draw.io (draw.io / app.diagrams.net):**
    *   *Fungsi:* Pembuat diagram alur (flowchart) berbasis web yang sangat rapi untuk laporan tugas siswa.
3.  **Blockly Games: Maze (blockly.games/maze):**
    *   *Fungsi:* Permainan labirin interaktif yang melatih konsep perulangan dan percabangan secara visual.
4.  **Replit (replit.com):**
    *   *Fungsi:* Browser-based Python interpreter yang ramah perangkat Chromebook/HP bagi siswa untuk mencoba latihan Python di atas tanpa perlu instalasi aplikasi di laptop.
5.  **W3Schools Python Quiz (w3schools.com/python/python_quiz.asp):**
    *   *Fungsi:* Kuis interaktif mengenai sintaks dasar Python.
