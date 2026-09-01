---
name: materi-minggu-4-jaringan-komputer-pengantar-dan-perangkat
description: Materi gabungan untuk Minggu 4 – Pengantar Komputer (tanpa ngoding), Jaringan Komputer, serta Pengetahuan Perangkat Jaringan.
metadata:
  type: user
---
# Materi Ajar – Minggu 4: Pengantar Komputer, Jaringan Komputer, & Perangkat Jaringan

---
## 1. Pengantar Komputer (Tanpa Ngoding)

### 1.1. Apa Itu Komputer?
Komputer adalah **mesin elektronik** yang dapat menerima data (input), memproses data, dan menghasilkan keluaran (output) secara otomatis.

#### 1.1.1. Komponen Utama
| Komponen | Fungsi Singkat |
|---|---|
| **CPU (Central Processing Unit)** | Otak komputer; mengeksekusi instruksi. |
| **RAM (Random Access Memory)** | Memori sementara untuk data yang sedang diproses. |
| **Storage (HDD/SSD)** | Menyimpan data secara permanen. |
| **Motherboard** | Papan sirkuit yang menghubungkan semua komponen. |
| **Power Supply Unit (PSU)** | Menyediakan listrik ke seluruh komponen. |
| **Input Device** | Keyboard, mouse, touchpad, scanner – mengirimkan data ke komputer. |
| **Output Device** | Monitor, printer, speaker – menampilkan hasil proses. |
| **Peripheral** | Perangkat tambahan seperti webcam, USB flash drive. |

### 1.2. Siklus Dasar Komputer
1. **Input** – Pengguna menekan tombol atau mengirim data lewat sensor.
2. **Proses** – CPU mengambil instruksi dari **memori**, mengeksekusinya menggunakan **ALU (Arithmetic Logic Unit)**.
3. **Storage** – Hasil sementara disimpan di **RAM**; hasil akhir disimpan ke **disk**.
4. **Output** – Data yang diproses ditampilkan di monitor atau perangkat lain.

### 1.3. Bilangan Biner & Representasi Data
- Semua data di dalam komputer diwakili oleh **0** dan **1** (biner).
- **Byte** = 8 bit, contoh: `01001101` = huruf ‘M’ dalam ASCII.
- **Konversi**: desimal ↔ biner (mis. 13 = 1101₂).

#### Aktivitas Unplugged
- **Kartu Biner:** Berikan masing‑masing kartu “0” atau “1”. Minta siswa menyusun 8 kartu menjadi satu byte dan menuliskan huruf yang diwakili (gunakan tabel ASCII sederhana).
- **Alur Proses:** Gambarkan alur **input → process → output** di papan tulis; masing‑masing siswa memegang satu kotak (CPU, RAM, Storage, Output) dan menggerakkan kartu data sesuai alur.

---
## 2. Jaringan Komputer (Tanpa Ngoding)

### 2.1. Apa Itu Jaringan Komputer?
Jaringan komputer adalah kumpulan **perangkat** (komputer, laptop, smartphone, printer, router, dll.) yang terhubung satu sama lain sehingga dapat **berbagi data** dan **sumber daya** (mis. file, printer, internet).

#### 2.1.1. Komponen Utama
- **Perangkat keras (hardware):** kartu jaringan (NIC), kabel, router, switch, atau akses poin Wi‑Fi.
- **Media transmisi:** kabel tembaga (UTP), serat optik, atau gelombang radio (Wi‑Fi).
- **Protokol:** aturan standar yang mengatur cara data dikirim dan diterima (contoh: TCP, IP).

### 2.2. Pengenalan IP (Internet Protocol)
- **IP** adalah **alamat** yang diberikan kepada setiap perangkat dalam jaringan supaya perangkat‑perangkat dapat menemukan satu sama lain, layaknya alamat rumah.
- Alamat IP biasanya ditulis dalam **format dotted decimal**, mis. `192.168.1.10`.
- **Fungsi utama IP:**
  1. **Identifikasi:** memberi identitas unik pada setiap perangkat.
  2. **Pengalamatan:** memungkinkan paket data menempuh jalur dari sumber ke tujuan.
- **Contoh sederhana:** Pada jaringan sekolah, semua komputer memiliki IP seperti `10.0.0.x` dimana `x` merupakan angka unik tiap komputer.

### 2.3. Model OSI – 7 Lapisan
| Lapisan | Fungsi Singkat |
|---|---|
| 7 – **Application** | Antarmuka pengguna (browser, email). |
| 6 – **Presentation** | Format data & enkripsi (mis. SSL). |
| 5 – **Session** | Mengatur sesi komunikasi (mulai & selesai). |
| 4 – **Transport** | Mengirim data secara terpecah (TCP/UDP). |
| 3 – **Network** | Menentukan jalur paket (IP). |
| 2 – **Data Link** | Mengatur pengiriman antar perangkat di jaringan lokal (Ethernet). |
| 1 – **Physical** | Media fisik (kabel, gelombang radio). |

> **Aktivitas sederhana:** Bagi kelas menjadi kelompok, masing‑masing dapatkan kartu berlabel lapisan OSI. Susun kartu secara urut, lalu beri contoh perangkat atau protokol yang berada pada tiap lapisan (mis. `Ethernet` pada lapisan 2, `IP` pada lapisan 3).

### 2.4. Model TCP/IP – 4 Lapisan (Ringkas)
| Lapisan | Nama | Keterangan |
|---|---|---|
| 4 – **Application** | Menggabungkan lapisan Application, Presentation, Session (HTTP, DNS, SMTP). |
| 3 – **Transport** | TCP / UDP – mengatur segmentasi dan keandalan. |
| 2 – **Internet** | IP – routing antar jaringan. |
| 1 – **Network Access** | Gabungan Physical & Data Link (Ethernet, Wi‑Fi). |

### 2.5. Arsitektur Client‑Server
- **Klien:** program yang **meminta** layanan (mis. web browser).
- **Server:** program yang **menyediakan** layanan (mis. web server).
- **Proses Interaksi (simplified):**
  1. Klien mengirim *request* (contoh: “GET /index.html”).
  2. Server memproses request, menghasilkan *response* (contoh: halaman HTML).
  3. Klien menampilkan response.

#### Diagram Mermaid (contoh pada slide)
```mermaid
sequenceDiagram
    participant Client as Klien
    participant Server as Server
    Client-&gt;&gt;Server: Request (HTTP GET /index.html)
    Server--&gt;&gt;Client: Response (HTML)
```

### 2.6. Praktik Mini – Socket Python (Sangat Ringkas)
Berikut contoh **client‑server** sederhana memakai modul `socket` di Python. Jalankan pada dua terminal (atau dua komputer) yang berada dalam jaringan yang sama.
```python
# socket_demo.py – contoh client‑server sederhana
import socket
HOST = '127.0.0.1'  # ganti dengan IP server bila di mesin lain
PORT = 65432        # port bebas (>1024)

choice = input('Run (s)erver or (c)lient? ')
if choice.lower().startswith('s'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Server listening...')
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            print('Received:', data.decode())
            conn.sendall(b'Pong')
else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Ping')
        data = s.recv(1024)
        print('Server replied:', data.decode())
```
**Tugas Praktik:**
1. Jalankan skrip sebagai *server* di satu terminal, lalu *client* di terminal lain.
2. Amati pesan “Ping” → “Pong”.
3. Diskusikan mengapa diperlukan **alamat IP** agar client dapat menemukan server.

### 2.7. Refleksi & Pertanyaan HOTS
- **Analisis:** Mengapa IP penting dalam jaringan? Apa yang terjadi bila dua perangkat memakai IP yang sama?
- **Evaluasi:** Dalam situasi jaringan Wi‑Fi yang lambat, faktor apa yang mungkin memengaruhi kecepatan?
- **Kreasi:** Gambar diagram jaringan sederhana kelas Anda (mis. 5 komputer + 1 router) dan beri label IP pada tiap perangkat.

---
## 3. Pengetahuan Perangkat Jaringan

### 3.1. LAN (Local Area Network)
- **Definisi:** Jaringan yang menghubungkan perangkat dalam area geografis kecil (kelas, laboratorium, rumah). Kecepatan tinggi (biasanya 100 Mbps – 10 Gbps) dan latensi rendah, biasanya menggunakan kabel **Ethernet** atau **Wi‑Fi**.
- **Contoh penggunaan:** Komputer di lab terhubung ke server file; siswa mengakses printer bersama.

### 3.2. Switch (Ethernet Switch)
- **Fungsi utama:** Menghubungkan banyak perangkat dalam satu LAN dan **mengirim paket data** hanya ke perangkat tujuan (menggunakan **MAC address**).
- **Keuntungan dibanding hub:**
  - **Segmentasi:** Hanya perangkat tujuan yang menerima data, mengurangi tabrakan.
  - **Kecepatan:** Full‑duplex (dua arah sekaligus).
- **Jenis switch:**
  - **Unmanaged:** Plug‑and‑play, tidak dapat dikonfigurasi.
  - **Managed:** Dapat dikonfigurasi (VLAN, QoS) – biasanya dipakai di jaringan sekolah atau kantor.

### 3.3. Access Point (AP)
- **Definisi:** Perangkat yang **menyediakan jaringan Wi‑Fi** dengan menghubungkan perangkat nirkabel ke jaringan kabel (biasanya ke switch).
- **Perbedaan dengan router wireless:**
  - **AP** hanya menambah kemampuan nirkabel pada jaringan yang sudah ada – tidak mengatur IP.
  - **Router wireless** biasanya memiliki fungsi routing (menghubungkan jaringan berbeda) sekaligus AP.
- **Fitur penting pada AP:**
  - **SSID** (nama jaringan) yang dapat disembunyikan atau dipublikasikan.
  - **Channel**: Frekuensi yang digunakan (2.4 GHz atau 5 GHz). Pilih channel yang tidak bentrok dengan AP lain.
  - **Keamanan:** WPA2‑PSK atau WPA3, enkripsi data.
- **Kegunaan dalam kelas:** Siswa dapat mengakses internet via laptop/tablet tanpa kabel.

### 3.4. Router
- **Fungsi utama:** Menghubungkan **dua jaringan yang berbeda** (mis. LAN sekolah dengan internet). 
- **Komponen dasar:**
  - **Interface WAN:** Terhubung ke ISP (Internet Service Provider).
  - **Interface LAN:** Terhubung ke switch atau AP untuk jaringan internal.
  - **Routing Table:** Menentukan jalur paket antara jaringan.
- **Fitur tambahan (umum pada router sekolah):**
  - **NAT (Network Address Translation):** Mengubah alamat IP internal menjadi satu alamat publik.
  - **DHCP Server:** Memberi alamat IP otomatis ke perangkat yang terhubung.
  - **Firewall:** Menyaring paket berbahaya.

### 3.5. Hub (Ethernet Hub) – Sejarah singkat
- **Definisi:** Perangkat jaringan yang **mengirimkan** setiap paket yang diterima ke **semua** port lain.
- **Kelemahan:** Banyak **tabrakan** (collision) karena semua perangkat berbagi satu saluran.
- **Penggunaan saat ini:** Sangat jarang; hampir seluruh jaringan modern memakai **switch**.

### 3.6. Modem (Modulator‑Demodulator)
- **Fungsi:** Mengubah sinyal digital dari komputer menjadi sinyal analog yang dapat dikirim melalui saluran telepon/kabel, dan sebaliknya.
- **Jenis:**
  - **DSL Modem, Cable Modem, Fiber ONT** – tergantung jenis layanan ISP.
- **Koneksi ke router:** Modem biasanya terhubung ke **WAN port** router untuk memberikan akses internet.

### 3.7. NIC (Network Interface Card)
- **Definisi:** Kartu atau modul yang memberikan **interface jaringan** ke komputer (Ethernet atau Wi‑Fi).
- **Komponen penting:**
  - **MAC address** unik tiap NIC.
  - **Port Ethernet RJ‑45** (untuk kabel) atau **antena Wi‑Fi**.
- **Penggunaan:** Semua komputer, laptop, atau Raspberry Pi membutuhkan NIC untuk bergabung ke jaringan.

### 3.8. Contoh Topologi Sederhana di Sekolah
```
[Modem] → [Router] → [Switch] → [PC 1]
                       ↘︎ [PC 2]
                       ↘︎ [AP] → [Laptop Wi‑Fi]
```
- **Modem** menghubungkan jaringan sekolah ke internet.
- **Router** mengatur lalu lintas antara jaringan internal dan internet.
- **Switch** menyebarkan koneksi kabel ke beberapa PC.
- **AP** memberi akses nirkabel ke perangkat mobile.

### 3.9. Pertanyaan Refleksi (untuk siswa)
1. Mengapa **switch** lebih efisien daripada **hub** dalam sebuah LAN?
2. Apa peran **MAC address** pada switch?
3. Bagaimana **router** dapat menghubungkan jaringan lokal dengan internet?
4. Sebutkan dua perbedaan utama antara **Access Point** dan **Router Wireless**.
5. Mengapa keamanan (WPA2/WPA3) penting pada **AP** di lingkungan sekolah?

---
*Materi ini kini terintegrasi dalam satu file Markdown, siap untuk dijadikan referensi RPP, lembar aktivitas, atau bahan presentasi.*
