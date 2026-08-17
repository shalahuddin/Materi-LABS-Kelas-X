# Bahan Ajar Detail: Jaringan Komputer, Internet, dan Keamanan Siber

*   **Mata Pelajaran:** Informatika
*   **Kelas/Fase:** X / E
*   **Alokasi Waktu:** Pendukung Modul 5 (Jaringan Komputer dan Internet)

---

## 1. Jaringan Lokal dan Internet

Jaringan komputer adalah sekumpulan perangkat komputer yang saling terhubung untuk berbagi data dan sumber daya (seperti file, printer, koneksi internet).

### A. Jaringan Lokal (Local Area Network - LAN)
*   **Definisi:** Jaringan komputer yang mencakup area geografis kecil/terbatas, seperti ruangan, rumah, sekolah, atau gedung kantor.
*   **Konektivitas:** Dapat menggunakan kabel (Ethernet) atau nirkabel (Wi-Fi).
*   **Karakteristik:** Memiliki kecepatan transfer data yang tinggi, latensi rendah, dan keamanan yang lebih mudah dikontrol karena berada di area privat.

### B. Internet (Interconnection-Networking)
*   **Definisi:** Jaringan komputer global yang menghubungkan miliaran komputer di seluruh dunia menggunakan protokol standar (TCP/IP).
*   **Karakteristik:** Bersifat publik, mencakup seluruh dunia, dan dapat diakses oleh siapa saja yang terhubung ke Internet Service Provider (ISP).

---

## 2. Klasifikasi Jaringan Komputer

Jaringan komputer diklasifikasikan berdasarkan beberapa aspek:

### A. Berdasarkan Jangkauan Geografis
1.  **PAN (Personal Area Network):** Jangkauan sangat dekat (beberapa meter), digunakan untuk perangkat pribadi. Contoh: Bluetooth antara HP dan headset.
2.  **LAN (Local Area Network):** Jangkauan gedung/sekolah.
3.  **MAN (Metropolitan Area Network):** Jangkauan satu kota (10-50 km). Contoh: Jaringan kantor cabang bank di satu kota.
4.  **WAN (Wide Area Network):** Jangkauan antar kota, negara, atau benua. Contoh: Jaringan internet global.

### B. Berdasarkan Media Transmisi Data
1.  **Jaringan Berkabel (Wired Network):** Menggunakan media fisik seperti kabel UTP (tembaga), kabel Koaksial, atau kabel Fiber Optik (serat kaca) untuk mengirimkan sinyal data.
2.  **Jaringan Nirkabel (Wireless Network):** Menggunakan gelombang elektromagnetik (Wi-Fi, gelombang radio, Bluetooth, inframerah, satelit) untuk mengirimkan data tanpa kabel fisik.

---

## 3. Topologi Jaringan Komputer

Topologi jaringan adalah pola hubungan geometris antar komputer/perangkat dalam jaringan.

### A. Topologi Bus
*   **Deskripsi:** Semua perangkat terhubung ke satu kabel utama (backbone).
*   **Kelebihan:** Murah, mudah diinstal untuk jaringan kecil.
*   **Kekurangan:** Jika kabel utama rusak/putus, seluruh jaringan mati. Deteksi kesalahan sangat sulit.

### B. Topologi Star (Bintang)
*   **Deskripsi:** Semua perangkat terhubung langsung ke perangkat pusat (Switch/Hub).
*   **Kelebihan:** Sangat andal. Jika satu komputer/kabel rusak, komputer lain tetap berjalan normal. Mudah mendeteksi kerusakan.
*   **Kekurangan:** Jika perangkat pusat (Switch/Hub) rusak, seluruh jaringan mati. Membutuhkan lebih banyak kabel.

### C. Topologi Ring (Cincin)
*   **Deskripsi:** Setiap komputer terhubung ke dua komputer di sebelahnya membentuk lingkaran tertutup.
*   **Kelebihan:** Aliran data lebih teratur karena searah.
*   **Kekurangan:** Jika salah satu komputer atau kabel rusak, komunikasi seluruh jaringan akan terputus.

### D. Topologi Mesh (Jala)
*   **Deskripsi:** Setiap komputer terhubung secara langsung ke setiap komputer lain dalam jaringan.
*   **Kelebihan:** Sangat aman (*redundancy* tinggi). Jika satu jalur putus, ada banyak jalur alternatif lain.
*   **Kekurangan:** Sangat mahal karena membutuhkan jumlah kabel dan port NIC yang sangat banyak. Rumit dikonfigurasi.

---

## 4. Komponen Jaringan Komputer

### A. Perangkat Keras (Hardware)
1.  **Router:** Menghubungkan beberapa jaringan yang berbeda (misalnya jaringan LAN sekolah dengan internet) dan merutekan lalu lintas data.
2.  **Switch:** Menghubungkan banyak perangkat dalam satu LAN yang sama dan mengirimkan data secara cerdas hanya ke perangkat tujuan berdasarkan alamat MAC.
3.  **Hub:** Mirip switch, tetapi mengirimkan data ke semua port secara membabi buta (menyebabkan tabrakan data / collision).
4.  **Access Point (AP):** Memancarkan sinyal Wi-Fi untuk menghubungkan perangkat nirkabel ke jaringan LAN berkabel.
5.  **NIC (Network Interface Card):** Kartu jaringan (Ethernet/Wi-Fi adapter) pada komputer agar bisa terhubung ke jaringan.
6.  **Kabel Jaringan:** 
    *   **UTP (Unshielded Twisted Pair):** Menggunakan tembaga, jarak maksimum ~100m.
    *   **Fiber Optic:** Menggunakan serat kaca, mentransmisikan data menggunakan cahaya, sangat cepat, tahan interferensi magnetik, jarak jauh (puluhan kilometer).

### B. Perangkat Lunak (Software) & Protokol
1.  **Sistem Operasi Jaringan:** OS yang didesain untuk server/router (seperti Linux, Windows Server, Cisco IOS, MikroTik RouterOS).
2.  **TCP/IP (Transmission Control Protocol/Internet Protocol):** Protokol standar komunikasi data di internet.
3.  **IP Address (Alamat IP):** Identitas numerik unik setiap perangkat di jaringan.
    *   **IPv4:** Berukuran 32-bit (contoh: `192.168.1.1`).
    *   **IPv6:** Berukuran 128-bit untuk mengatasi kehabisan alamat IPv4 (contoh: `2001:db8::ff00:42:8329`).
4.  **DNS (Domain Name System):** Buku telepon internet yang menerjemahkan nama domain (seperti `google.com`) menjadi alamat IP (seperti `142.250.190.46`).

---

## 5. Keamanan Siber (Cyber Security)

### A. Definisi & Manfaat
Keamanan siber adalah praktik melindungi sistem, jaringan, program, dan data dari serangan digital.
*   **Manfaat:**
    *   Mencegah kebocoran data pribadi dan rahasia perusahaan.
    *   Menjaga kelangsungan layanan digital (mencegah sistem down/rusak).
    *   Melindungi reputasi dan mencegah kerugian finansial akibat penipuan digital.

### B. Cara Kerja Keamanan Siber
Menggunakan prinsip **CIA Triad**:
1.  **Confidentiality (Kerahasiaan):** Memastikan hanya orang yang berhak yang bisa membaca data (menggunakan enkripsi).
2.  **Integrity (Integritas):** Memastikan data tidak diubah di tengah jalan oleh pihak luar (menggunakan hashing/checksum).
3.  **Availability (Ketersediaan):** Memastikan sistem/data selalu bisa diakses saat dibutuhkan (menggunakan backup dan perlindungan anti-DDoS).

### C. Jenis & Metode Ancaman Siber (Cyber Threats)
1.  **Malware (Malicious Software):** Program jahat yang merusak sistem.
    *   *Virus/Worm:* Menggandakan diri untuk merusak file dan jaringan.
    *   *Ransomware:* Mengenkripsi data pengguna dan meminta uang tebusan untuk membukanya.
    *   *Trojan Horse:* Menyamar sebagai aplikasi baik untuk membuka pintu belakang bagi peretas.
2.  **Phishing:** Upaya memancing korban untuk memberikan informasi sensitif (seperti password/PIN) dengan menyamar sebagai pihak tepercaya (melalui email/website palsu).
3.  **DDoS (Distributed Denial of Service):** Membanjiri lalu lintas server dengan jutaan request palsu hingga server overload dan tidak bisa diakses pengguna asli.
4.  **Social Engineering (Rekayasa Sosial):** Menipu korban secara psikologis agar membocorkan password atau kode OTP, alih-alih meretas sistem secara teknis.

### D. Pencegahan Cyber Crime
*   **Firewall:** Filter lalu lintas jaringan untuk mencegah akses tidak sah dari luar.
*   **Password Kuat & Pengelola Kata Sandi:** Hindari password mudah ditebak seperti `123456` atau `tanggal lahir`.
*   **Autentikasi Dua Langkah (2FA/MFA):** Membutuhkan verifikasi tambahan (seperti kode SMS/aplikasi authenticator) selain password.
*   **Pembaruan Sistem secara Rutin:** Menambal celah keamanan sistem operasi dan software.
*   **Antivirus/Antimalware:** Melakukan scan dan membersihkan file berbahaya.
*   **Enkripsi SSL/TLS:** Selalu gunakan website dengan awalan `https://` (ikon gembok terkunci) untuk mengenkripsi transmisi data.

---

## 6. Tata Kelola Data (Data Governance)

Tata kelola data adalah pengelolaan ketersediaan, kegunaan, integritas, dan keamanan data dalam organisasi.

### A. Penguatan & Keamanan Database (Database Hardening)
1.  **Enkripsi Data At Rest:** Mengenkripsi database yang disimpan di harddisk sehingga tidak dapat dibaca jika harddisk dicuri.
2.  **Pencegahan SQL Injection (SQLi):** Menulis kode program web secara aman agar peretas tidak bisa menyisipkan perintah SQL jahat ke form input web untuk membocorkan database.
3.  **Backup Data Berkala:** Menyimpan salinan database di lokasi terpisah (cloud atau server offline) untuk pemulihan jika terjadi bencana atau serangan ransomware.

### B. Keamanan Transmisi Data
1.  **VPN (Virtual Private Network):** Membuat terowongan enkripsi privat yang aman saat kita mengakses internet melalui jaringan publik/Wi-Fi gratis.
2.  **WPA3:** Protokol keamanan enkripsi terbaru untuk jaringan nirkabel (Wi-Fi) untuk mencegah peretas menyadap data nirkabel.
3.  **SSL/TLS (HTTPS):** Mengamankan pertukaran data antara browser web pengguna dengan web server.

### C. Tata Kelola Akses (Access Governance)
1.  **RBAC (Role-Based Access Control):** Membatasi hak akses berdasarkan peran pengguna. Contoh: Siswa hanya bisa membaca data nilai (*read-only*), sementara guru bisa menulis dan mengubah data nilai (*read-write*). Admin memiliki hak penuh.
2.  **AAA (Authentication, Authorization, Accounting):**
    *   *Authentication:* Membuktikan siapa Anda (misal: dengan username & password).
    *   *Authorization:* Menentukan apa yang boleh Anda lakukan (hak akses).
    *   *Accounting:* Mencatat log apa saja yang telah Anda lakukan di dalam sistem.

---

## 🌐 Referensi Website Latihan Siswa

1.  **Cisco Packet Tracer (netacad.com / free course):**
    *   *Fungsi:* Simulator desain jaringan komputer gratis yang sangat kuat.
    *   *Cara pakai:* Siswa diajak merancang topologi star dengan menempatkan 1 Switch, 3 PC, dan melakukan konfigurasi IP Address sederhana untuk tes ping antarkomputer.
2.  **Cisco Binary Game (binarygame.cisco.com):**
    *   *Fungsi:* Game edukatif cepat untuk belajar konversi angka biner ke desimal (sangat penting untuk konsep IP Address dan subnetting).
3.  **PortSwigger Web Security Academy (portswigger.net/web-security):**
    *   *Fungsi:* Kursus interaktif dasar keamanan web gratis (bagi siswa yang berminat lebih lanjut pada keamanan siber).
4.  **W3Schools Cyber Security (w3schools.com/cybersecurity):**
    *   *Fungsi:* Latihan kuis interaktif mengenai terminologi keamanan siber dasar.
5.  **DNS Speed Test / Trace Route Tools (mxtoolbox.com atau aplikasi CMD):**
    *   *Fungsi:* Praktik menggunakan perintah `ping`, `nslookup`, dan `tracert` di terminal komputer untuk melacak rute pengiriman data di internet.
