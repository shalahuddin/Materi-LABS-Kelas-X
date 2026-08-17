# Bahan Ajar Detail: Pemrograman Web Dasar (HTML, CSS, dan JavaScript)

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Alokasi Waktu:** Pendukung Modul 8 (Pemrograman Web)

---

## Pendahuluan
Sebuah halaman web modern dibangun menggunakan tiga pilar utama teknologi:
1.  **HTML (HyperText Markup Language):** Sebagai **kerangka** atau struktur utama halaman web (ibarat tulang manusia).
2.  **CSS (Cascading Style Sheets):** Sebagai **penghias** atau pengatur tata letak, warna, dan font halaman web (ibarat pakaian dan kulit manusia).
3.  **JavaScript (JS):** Sebagai **otak** yang memberikan interaktivitas atau perilaku dinamis pada halaman web (ibarat otot dan sistem saraf manusia yang merespons aksi).

---

## 1. HTML (Kerangka Web)

HTML ditulis menggunakan sepasang **tag** yang ditandai dengan kurung siku (`<tag_pembuka>` dan `</tag_penutup>`).

### A. Struktur Dasar Dokumen HTML
Setiap file HTML wajib memiliki kerangka dasar berikut:
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Judul Halaman Web</title>
</head>
<body>
    <!-- Seluruh isi halaman web diletakkan di sini -->
</body>
</html>
```

### B. Tag-Tag HTML Dasar yang Penting
1.  **Heading (`<h1>` sampai `<h6>`):** Menandakan judul atau subjudul halaman web. `<h1>` adalah yang terbesar dan `<h6>` adalah yang terkecil.
2.  **Paragraf (`<p>`):** Digunakan untuk menulis teks paragraf.
3.  **Link/Tautan (`<a href="URL">Teks</a>`):** Menghubungkan halaman web ke halaman lain atau website luar.
4.  **Gambar (`<img src="gambar.jpg" alt="Penjelasan">`):** Menampilkan gambar. Tag ini tidak memiliki tag penutup (*self-closing*).
5.  **Daftar/List:**
    *   `<ul>` (*Unordered List*): Daftar dengan bullet bulat/simbol.
    *   `<ol>` (*Ordered List*): Daftar dengan angka/urutan huruf.
    *   `<li>` (*List Item*): Elemen di dalam daftar.
6.  **Container/Pembungkus (`<div>`):** Digunakan untuk mengelompokkan elemen HTML agar mudah diatur tata letaknya menggunakan CSS.
7.  **Formulir (`<form>`):** Tempat input data dari pengguna, seperti tombol (`<button>`) dan kotak input teks (`<input type="text">`).

---

## 2. CSS (Tampilan Web)

CSS digunakan untuk mengubah tampilan dan tata letak elemen HTML. CSS dapat ditulis di dalam file terpisah (`style.css`) atau di dalam tag `<style>` di bagian `<head>`.

### A. Selector Dasar CSS
Selector menentukan elemen mana yang ingin kita ubah gayanya:
```css
/* 1. Element Selector (berdasarkan tag HTML langsung) */
p {
    color: darkgray; /* mengubah warna teks seluruh paragraf */
}

/* 2. Class Selector (diawali tanda titik, digunakan berulang kali) */
.warna-teks-merah {
    color: red;
}

/* 3. ID Selector (diawali tanda pagar, unik untuk satu elemen saja) */
#tombol-utama {
    background-color: blue;
}
```

### B. Properti CSS Utama
1.  **Warna & Latar:** `color` (warna teks), `background-color` (warna latar belakang).
2.  **Tipografi:** `font-family` (jenis font), `font-size` (ukuran huruf), `text-align` (posisi teks: center/left/right).
3.  **Box Model (Kotak Elemen):**
    *   `padding`: Jarak antara konten dengan border di dalam kotak.
    *   `margin`: Jarak antara kotak elemen dengan elemen luar lainnya.
    *   `border`: Garis tepi kotak.
4.  **Tata Letak Dasar (Flexbox):**
    Menggunakan properti `display: flex;` pada kontainer untuk mengatur elemen-elemen di dalamnya berjejer secara horizontal atau vertikal dengan rapi.

---

## 3. JavaScript (Interaktivitas Web)

JavaScript membuat halaman web merespons tindakan pengguna (seperti klik tombol, input teks, dll.). JavaScript dapat ditulis di dalam tag `<script>`.

### A. Variabel & Fungsi Dasar
```javascript
// Deklarasi Variabel
let nama = "Budi"; // Nilai bisa diubah
const kkm = 75;    // Nilai tetap (konstan)

// Membuat Fungsi
function sapaPengguna() {
    alert("Halo " + nama + ", selamat belajar JavaScript!");
}
```

### B. Manipulasi DOM (Document Object Model) Sederhana
DOM manipulasi adalah cara JavaScript mengubah konten HTML secara dinamis.
*Contoh:* Mengubah teks paragraf saat sebuah tombol diklik.
```html
<p id="paragraf-salam">Ini adalah teks lama.</p>
<button onclick="ubahTeks()">Klik Saya</button>

<script>
function ubahTeks() {
    // Mencari elemen HTML dengan id 'paragraf-salam' dan mengubah isinya
    document.getElementById("paragraf-salam").innerHTML = "Halo! Teks ini berhasil diubah oleh JavaScript!";
}
</script>
```

---

## 4. Proyek Praktik: Membuat Halaman Portofolio Pribadi Sederhana

Buatlah sebuah berkas bernama `index.html` dan ketikkan kode berikut. Buka berkas tersebut menggunakan browser web Anda untuk melihat hasilnya.

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Portofolio Pribadi Saya</title>
    <style>
        /* Gaya CSS */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .biodata {
            margin-bottom: 20px;
        }
        .skills-list {
            display: flex;
            gap: 10px;
        }
        .skill-badge {
            background-color: #3498db;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
        }
        button {
            background-color: #27ae60;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #219150;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>Portofolio Pribadi Saya</h1>
        <p>Siswa SMA Kelas X | Pecinta Teknologi</p>
    </div>

    <div class="container">
        <div class="biodata">
            <h2>Tentang Saya</h2>
            <p id="deskripsi-diri">Saya adalah siswa kelas X SMA yang sedang belajar dasar-dasar pemrograman web. Saya suka mempelajari hal baru mengenai teknologi informasi.</p>
        </div>

        <h2>Keahlian Saya</h2>
        <div class="skills-list">
            <span class="skill-badge">HTML 5</span>
            <span class="skill-badge">CSS 3</span>
            <span class="skill-badge">Python</span>
        </div>

        <br><hr><br>

        <h2>Interaktivitas (JavaScript)</h2>
        <p>Klik tombol di bawah untuk mengubah bahasa deskripsi diri menjadi Bahasa Inggris secara otomatis!</p>
        <button onclick="terjemahkanDiri()">Terjemahkan (Translate)</button>
    </div>

    <script>
        // Kode JavaScript
        function terjemahkanDiri() {
            const teksDeskripsi = document.getElementById("deskripsi-diri");
            teksDeskripsi.innerHTML = "I am a tenth-grade high school student currently learning the basics of web programming. I love to explore new things about information technology.";
            teksDeskripsi.style.color = "#27ae60";
            alert("Deskripsi diri berhasil diterjemahkan!");
        }
    </script>

</body>
</html>
```

---

## 🌐 Referensi Website Latihan Siswa

1.  **W3Schools HTML / CSS / JS (w3schools.com):**
    *   *Fungsi:* Tutorial interaktif terlengkap dan ramah pemula dengan editor kode bawaan (*Try It Yourself*).
2.  **Codepen (codepen.io):**
    *   *Fungsi:* Sandbox pemrograman web online terpopuler. Siswa bisa mengetikkan kode HTML, CSS, dan JS di tab terpisah dan langsung melihat hasilnya secara real-time di bagian bawah layar tanpa perlu menyimpan file lokal.
3.  **freeCodeCamp (freecodecamp.org):**
    *   *Fungsi:* Kursus web development interaktif berbasis browser yang sepenuhnya gratis untuk mendapatkan sertifikasi.
4.  **JSFiddle (jsfiddle.net):**
    *   *Fungsi:* Playground alternatif sederhana untuk kolaborasi coding web secara online.
