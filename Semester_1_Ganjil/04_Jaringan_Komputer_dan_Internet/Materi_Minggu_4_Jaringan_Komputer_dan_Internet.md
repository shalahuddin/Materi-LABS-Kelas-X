---
name: materi-minggu-4-jaringan-komputer-dan-internet
description: Modul Bahan Ajar Komprehensif Minggu 4 Informatika Kelas X SMA (Kurikulum Merdeka) - Jaringan Komputer, Internet, Komponen, Topologi, Protokol, Cyber Security, dan Tata Kelola Keamanan Data.
metadata:
  type: reference
---

# 🌐 MODUL BAHAN AJAR SISWA: JARINGAN KOMPUTER & INTERNET
**Mata Pelajaran:** Informatika  
**Fase / Kelas / Semester:** E / X (Sepuluh) / Ganjil  
**Alokasi Waktu:** 4 Jam Pelajaran (2 Pertemuan × 2 JP)  
**Model Pembelajaran:** *Deep Learning* (Mindful, Meaningful, Joyful)

---

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, peserta didik diharapkan mampu:
1. **Menjelaskan** konsep dasar jaringan komputer, perbedaan jaringan lokal (LAN) dan internet (WAN), serta cara kerja pengiriman data.
2. **Mengidentifikasi & Membandingkan** klasifikasi jaringan (PAN, LAN, MAN, WAN) dan topologi jaringan fisik (Bus, Star, Ring, Mesh, Tree, Hybrid).
3. **Menganalisis** fungsi komponen perangkat keras (Router, Switch, Access Point, Modem, NIC, Kabel UTP/Fiber) dan perangkat lunak jaringan (TCP/IP, Model OSI, DNS, DHCP).
4. **Menerapkan & Mengevaluasi** prinsip *Cyber Security* (ancaman siber, metode proteksi, enkripsi, firewall) dan tata kelola keamanan data pribadi dalam kehidupan sehari-hari.

---

## 📖 DAFTAR ISI
1. [BAB 1: Pengantar Jaringan Komputer & Internet](#bab-1-pengantar-jaringan-komputer--internet)
2. [BAB 2: Klasifikasi Jaringan Berdasarkan Jangkauan Geografis](#bab-2-klasifikasi-jaringan-berdasarkan-jangkauan-geografis)
3. [BAB 3: Topologi Jaringan Komputer](#bab-3-topologi-jaringan-komputer)
4. [BAB 4: Komponen Jaringan Komputer (Hardware & Software)](#bab-4-komponen-jaringan-komputer-hardware--software)
5. [BAB 5: Model Protokol Jaringan (OSI vs TCP/IP) & Cara Kerja Web](#bab-5-model-protokol-jaringan-osi-vs-tcpip--cara-kerja-web)
6. [BAB 6: Keamanan Siber (Cyber Security) & Tata Kelola Data](#bab-6-keamanan-siber-cyber-security--tata-kelola-data)
7. [BAB 7: Studi Kasus HOTS & Refleksi Kritis](#bab-7-studi-kasus-hots--refleksi-kritis)
8. [Rangkuman Materi & Glosarium](#rangkuman-materi--glosarium)

---

## BAB 1: Pengantar Jaringan Komputer & Internet

### 1.1. Mengapa Perangkat Perlu Terhubung?
Bayangkan jika smartphone atau laptop Anda tidak terhubung ke jaringan mana pun. Anda hanya bisa mengetik dokumen offline atau bermain game sendirian. Begitu perangkat terhubung ke jaringan:
- Anda dapat mengirim pesan instan dalam hitungan milidetik.
- Seluruh siswa di laboratorium sekolah dapat mencetak dokumen ke satu printer bersama tanpa harus memindahkan flashdisk (*resource sharing*).
- Komputer dapat mengambil data dari server di belahan dunia lain.

> 💡 **Definisi Jaringan Komputer:**  
> Sistem yang terdiri atas dua atau lebih perangkat komputasi (komputer, smartphone, server, printer pintar) yang saling terhubung menggunakan media transmisi (kabel atau nirkabel) untuk saling bertukar data, informasi, dan berbagi sumber daya (*hardware/software*).

```
   [Komputer Siswa 1] ──┐
   [Komputer Siswa 2] ──┼──> [Switch Jaringan] ──> [Printer Bersama / Server Sekolah]
   [Smartphone Guru]  ──┘
```

---

### 1.2. Jaringan Lokal (LAN) vs. Internet (Jaringan Global)

| Aspek Pembeda | Jaringan Lokal (LAN / Intranet) | Jaringan Internet (Global Network) |
|---|---|---|
| **Cakupan Wilayah** | Terbatas (satu ruangan, laboratorium, rumah, atau satu gedung sekolah). | Seluruh dunia (lintas benua, negara, dan planet via satelit). |
| **Kepemilikan** | Milik pribadi / lembaga sekolah sendiri. | Milik publik (kumpulan ribuan penyedia jaringan / ISP yang terhubung). |
| **Akses & Keamanan** | Terisolasi & privat; hanya pengguna terdaftar di sekolah yang bisa masuk. | Terbuka untuk umum; membutuhkan pengamanan ekstra (*firewall* & enkripsi). |
| **Kecepatan & Latensi**| Sangat cepat (100 Mbps – 10 Gbps) dengan latensi sangat rendah (< 5 ms). | Tergantung bandwidth ISP dan jarak server (latensi 15 – 300+ ms). |
| **Ketergantungan ISP** | Tetap bisa bertukar file meski kabel internet luar negeri putus. | Wajib menggunakan langganan ISP (*Internet Service Provider*). |

---

## BAB 2: Klasifikasi Jaringan Berdasarkan Jangkauan Geografis

Untuk memudahkan perancangan, jaringan dikelompokkan berdasarkan luas jangkauan fisiknya:

```
┌────────────────────────────────────────────────────────────────────────┐
│  WAN (Wide Area Network): Seluruh Dunia / Lintas Benua                 │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  MAN (Metropolitan Area Network): Satu Kota (10 - 50 km)         │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │  LAN (Local Area Network): Satu Gedung / Lab (10 m - 1 km) │  │  │
│  │  │  ┌──────────────────────────────────────────────────────┐  │  │  │
│  │  │  │  PAN (Personal Area Network): Sekitar Tubuh (< 10 m) │  │  │  │
│  │  │  └──────────────────────────────────────────────────────┘  │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

1. **PAN (*Personal Area Network*):**
   - Jangkauan: Kurang dari 10 meter (area pribadi).
   - Media: Bluetooth, Wi-Fi Direct, USB, NFC.
   - Contoh: Menghubungkan TWS/Headset nirkabel ke smartphone, transfer file AirDrop/QuickShare, koneksi smartwatch.
2. **LAN (*Local Area Network*):**
   - Jangkauan: 10 meter s.d. 1 kilometer (satu ruangan, laboratorium, rumah, kampus).
   - Media: Kabel UTP (Ethernet) dan Wi-Fi (WLAN).
   - Contoh: Jaringan komputer laboratorium CBT SMA LABS.
3. **MAN (*Metropolitan Area Network*):**
   - Jangkauan: 10 s.d. 50 kilometer (mencakup satu kawasan kota atau wilayah metropolitan).
   - Media: Kabel Fiber Optic bawah tanah atau gelombang mikro nirkabel (*microwave radio link*).
   - Contoh: Jaringan CCTV Dinas Perhubungan satu kota, jaringan antar-kantor cabang Bank Mandiri se-Jabodetabek.
4. **WAN (*Wide Area Network*):**
   - Jangkauan: Lintas pulau, negara, benua, hingga skala global.
   - Media: Kabel serat optik bawah laut (*submarine cable*), satelit geostasioner / Starlink.
   - Contoh: Jaringan global **Internet**, jaringan perbankan global (SWIFT).

---

## BAB 3: Topologi Jaringan Komputer

Topologi jaringan adalah **peta susunan atau pola geometris** bagaimana perangkat-perangkat komputer saling dihubungkan satu sama lain secara fisik.

```
       [TOPOLOGI BUS]                      [TOPOLOGI STAR]
  ===┬===========┬===========┬===                [PC 1]
     │           │           │                     │
   [PC1]       [PC2]       [PC3]         [PC4] ──[SWITCH]── [PC2]
  (Satu kabel utama / Backbone)                    │
                                                 [PC3]
```

### Tabel Perbandingan Lengkap Topologi Jaringan

| Nama Topologi | Ciri-Ciri Fisik | Kelebihan | Kekurangan | Penggunaan Nyata |
|---|---|---|---|---|
| **Star (Bintang)** *(Paling Populer)* | Semua komputer terhubung langsung ke satu perangkat pusat (**Switch / Hub**). | ✅ Mudah dipasang & dikelola.<br>✅ Jika 1 kabel PC putus, PC lain tidak terganggu.<br>✅ Deteksi kerusakan sangat mudah. | ❌ Butuh banyak kabel.<br>❌ Jika Switch pusat mati, seluruh jaringan ikut lumpuh. | Standar utama Lab Komputer Sekolah, Kantor, dan Rumah modern. |
| **Bus (Jalur Linear)** | Menggunakan **satu kabel utama (backbone)** panjang dengan terminator di kedua ujungnya. | ✅ Hemat kabel dan biaya murah.<br>✅ Sangat sederhana untuk jaringan darurat kecil. | ❌ Rentan tabrakan data (*collision*).<br>❌ Jika kabel utama putus, seluruh jaringan mati.<br>❌ Sulit mencari titik kerusakan. | Jaringan lama kabel Coaxial (10Base2), sistem sensor IoT sederhana. |
| **Ring (Cincin)** | Komputer terhubung melingkar membentuk cincin tertutup. Data bergerak satu arah via *token*. | ✅ Aliran data tertib (tidak ada tabrakan data).<br>✅ Performa tetap stabil saat beban trafik padat. | ❌ Jika 1 komputer mati, seluruh loop cincin putus.<br>❌ Menambah perangkat baru harus memutus jaringan sementara. | Jaringan serat optik *backbone* berkecepatan tinggi (FDDI / SONET Ring). |
| **Mesh (Jala Penuh)** | Setiap komputer terhubung langsung dengan kabel khusus ke **setiap** komputer lain (*Point-to-Point*). | ✅ Toleransi kesalahan (*fault-tolerance*) tertinggi.<br>✅ Jika 1 jalur putus, masih ada ratusan jalur alternatif.<br>✅ Privasi & keamanan sangat tinggi. | ❌ Biaya kabel & port sangat mahal.<br>❌ Pemasangan dan instalasi sangat rumit (Rumus jalur: $\frac{n(n-1)}{2}$). | Jaringan kritis militer, sistem interkoneksi antar *core router* ISP. |
| **Tree (Pohon/Hierarki)** | Kombinasi beberapa topologi Star yang dihubungkan ke kabel utama (Backbone) bertingkat. | ✅ Mudah diskalakan (menambah cabang/gedung baru).<br>✅ Manajemen data terbagi per departemen/lantai. | ❌ Bergantung pada *switch root* (akar utama). Jika hub induk mati, seluruh cabang bawah mati. | Jaringan kampus bertingkat, jaringan instansi pemerintah berjenjang. |
| **Hybrid (Campuran)** | Penggabungan dua atau lebih jenis topologi yang berbeda (misal Star + Ring + Mesh). | ✅ Sangat fleksibel mengikuti arsitektur bangunan.<br>✅ Efisien untuk organisasi besar. | ❌ Perancangan dan konfigurasi perangkat lunak rumit. Biaya relatif tinggi. | Jaringan perusahaan multinasional / provider telekomunikasi. |

---

## BAB 4: Komponen Jaringan Komputer (Hardware & Software)

Agar jaringan dapat beroperasi, dibutuhkan sinergi antara perangkat keras (*Hardware*) dan perangkat lunak (*Software & Protokol*).

```
 ┌──────────────┐      ┌─────────────┐      ┌────────────┐      ┌──────────────┐
 │  INTERNET    │ ───> │ MODEM (ONT) │ ───> │   ROUTER   │ ───> │    SWITCH    │
 │ (Dunia Luar) │ Fiber│  (Sinyal)   │ WAN  │ (IP & NAT) │ LAN  │ (Distribusi) │
 └──────────────┘      └─────────────┘      └────────────┘      └──────┬───────┘
                                                                       │
                         ┌───────────────────────┬─────────────────────┴──────────────┐
                         ▼                       ▼                                    ▼
                  [PC Laboratorium 1]     [PC Laboratorium 2]                   [ACCESS POINT (Wi-Fi)]
                     (Kabel UTP)             (Kabel UTP)                          │ (Gelombang Radio)
                                                                                  ▼
                                                                           [Smartphone Siswa]
```

### 4.1. Perangkat Keras Jaringan (Hardware)

1. **Router (Pengarah Jalur):**
   - **Fungsi Utama:** Menghubungkan dua atau lebih **jaringan yang berbeda subnet/jaringan luar** (misal menghubungkan LAN sekolah ke WAN Internet).
   - **Fitur Cerdas:** Memiliki tabel routing (*routing table*), menjalankan layanan **NAT** (*Network Address Translation*), membagikan IP via **DHCP Server**, dan menjadi benteng awal pertahanan (**Firewall**).
2. **Switch (Penyambung Cerdas):**
   - **Fungsi Utama:** Menghubungkan banyak komputer dalam **satu LAN yang sama**.
   - **Cara Kerja:** Merekam **MAC Address** (*Media Access Control*) setiap komputer pada tabel memorinya (*MAC Table*). Ketika data datang untuk Komputer B, Switch hanya mengirimkan data ke kabel port Komputer B (tidak membocorkannya ke komputer lain).
   - *Beda Switch vs Hub:* Hub adalah perangkat lama yang 'bodoh' (membroadcast paket ke semua port sehingga menimbulkan tabrakan/collision), sedangkan Switch cerdas dan efisien (*full-duplex*).
3. **Access Point (AP - Pemancar Nirkabel):**
   - **Fungsi Utama:** Mengubah media kabel (Ethernet) menjadi gelombang radio nirkabel (**Wi-Fi**) frekuensi 2.4 GHz atau 5 GHz sehingga perangkat mobile (laptop, smartphone) bisa terhubung.
4. **Modem & ONT (Modulator Demodulator / Optical Network Terminal):**
   - **Fungsi Utama:** Mengubah sinyal dari penyedia layanan internet (sinyal cahaya pada kabel Fiber Optic atau sinyal analog pada telepon) menjadi sinyal digital yang dimengerti router.
5. **NIC (Network Interface Card / Kartu Jaringan):**
   - **Fungsi:** Komponen chip pada motherboard komputer/laptop yang menyediakan colokan kabel LAN (RJ-45) atau antena Wi-Fi. Memiliki identitas fisik permanen bernama **MAC Address** (contoh: `00:1A:2B:3C:4D:5E`).
6. **Media Transmisi Fisik:**
   - **Kabel UTP (Unshielded Twisted Pair) Cat 6:** Kabel tembaga berpilin dengan colokan RJ-45. Jarak maksimal 100 meter per tarikan kabel.
     - *Kabel Straight-Through:* Untuk menghubungkan perangkat berbeda (PC ke Switch).
     - *Kabel Crossover:* Untuk menghubungkan perangkat sejenis (PC langsung ke PC tanpa switch).
   - **Kabel Fiber Optic (Serat Optik):** Mengirimkan data menggunakan denyut **cahaya kaca**. Kecepatan hingga puluhan Gbps, jarak puluhan kilometer, dan kebal dari interferensi petir/listrik.

---

### 4.2. Perangkat Lunak Jaringan (Software & Layanan)

1. **Sistem Operasi Jaringan (Network OS):** Software khusus server dan router (misal: Linux Ubuntu Server, Cisco IOS, MikroTik RouterOS, Windows Server).
2. **Layanan DHCP (*Dynamic Host Configuration Protocol*):** Robot otomatis di router yang meminjamkan alamat IP ke komputer siswa secara otomatis saat tersambung ke Wi-Fi.
3. **Layanan DNS (*Domain Name System*):** 'Buku telepon' internet yang menerjemahkan nama domain manusiawi (seperti `www.kemdikbud.go.id`) menjadi alamat angka IP komputer server (seperti `118.98.228.68`).
4. **Web Server & Web Browser (Arsitektur Client-Server):**
   - *Client (Browser):* Meminta halaman web dengan protokol HTTP/HTTPS (`GET /index.html`).
   - *Server (Web Server seperti Nginx/Apache):* Memproses dan mengirimkan berkas HTML, CSS, JavaScript ke pengguna.

---

## BAB 5: Model Protokol Jaringan (OSI vs TCP/IP) & Cara Kerja Web

Komunikasi data di internet dapat terjadi karena adanya standarisasi protokol bertingkat (*layered architecture*).

### 5.1. Model 7 Lapis OSI (*Open Systems Interconnection*) vs Model TCP/IP

```
    [MODEL OSI - 7 LAPISAN]                 [MODEL TCP/IP - 4 LAPISAN]
 ┌───────────────────────────────┐        ┌───────────────────────────────┐
 │ 7. Application  (HTTP, DNS)   │ ───┐   │                               │
 │ 6. Presentation (SSL, JPG)    │ ───┼──>│ 4. Application (HTTP, DNS)    │
 │ 5. Session      (Socks, RPC)  │ ───┘   │                               │
 ├───────────────────────────────┤        ├───────────────────────────────┤
 │ 4. Transport    (TCP, UDP)    │ ──────>│ 3. Transport (TCP, UDP)       │
 ├───────────────────────────────┤        ├───────────────────────────────┤
 │ 3. Network      (IP, Router)  │ ──────>│ 2. Internet (IP, Routing)     │
 ├───────────────────────────────┤        ├───────────────────────────────┤
 │ 2. Data Link    (MAC, Switch) │ ───┐   │ 1. Network Access             │
 │ 1. Physical     (Kabel, Bit)  │ ───┴──>│    (Ethernet, Wi-Fi, Kabel)   │
 └───────────────────────────────┘        └───────────────────────────────┘
```

#### Jembatan Keledai Menghafal Lapisan OSI:
> *"**A**nak **P**ak **S**oleh **T**idak **N**akal **D**an **P**intar"*  
> (**A**pplication $\rightarrow$ **P**resentation $\rightarrow$ **S**ession $\rightarrow$ **T**ransport $\rightarrow$ **N**etwork $\rightarrow$ **D**ata Link $\rightarrow$ **P**hysical)

#### Peran Setiap Lapisan OSI:
1. **Physical:** Mengubah data menjadi sinyal listrik/cahaya/radio (Kabel, Port, Konektor).
2. **Data Link:** Mengatur pengiriman data antar perangkat yang bertetangga fisik via MAC Address (Switch, Kartu LAN).
3. **Network:** Memberi alamat logika (**Alamat IP**) dan memilih jalur rute tercepat antar jaringan (Router, Protokol IP).
4. **Transport:** Memecah data menjadi paket kecil (*segmentation*), memastikan tidak ada paket yang hilang (**TCP** = andal dan bergaransi; **UDP** = super cepat untuk game online/live streaming).
5. **Session:** Membuka, menjaga, dan menutup koneksi komunikasi antar program.
6. **Presentation:** Menerjemahkan format data, kompresi, dan enkripsi keamanan (SSL/TLS, format JPEG/MP4).
7. **Application:** Aplikasi yang berinteraksi langsung dengan manusia (Chrome, WhatsApp, Email).

---

### 5.2. Memahami Alamat IP (*Internet Protocol Address*)

Alamat IP adalah identitas numerik unik untuk setiap perangkat.
- **Format IPv4:** Terdiri dari 32 bit yang dibagi menjadi 4 blok angka desimal (0-255).  
  *Contoh:* `192.168.1.15`
- **Pembagian IP Privat vs IP Publik:**
  - **IP Privat:** Alamat khusus yang hanya berlaku di jaringan lokal (misal: `192.168.x.x`, `10.x.x.x`, `172.16.x.x`). Komputer luar internet tidak bisa langsung mengakses IP ini.
  - **IP Publik:** Alamat resmi yang diberikan ISP untuk mengakses internet global.
- **Peran NAT (*Network Address Translation*):** Router bertindak seperti petugas pos yang mengubah ratusan IP privat siswa di sekolah menjadi 1 IP publik resmi saat mengakses internet.

---

## BAB 6: Keamanan Siber (Cyber Security) & Tata Kelola Data

Ketika perangkat kita terhubung ke internet, perangkat tersebut juga terhubung dengan jutaan potensi ancaman kejahatan digital (*Cyber Crime*).

### 6.1. Mengapa Cyber Security Sangat Penting?
Keamanan siber berpegang pada prinsip **CIA Triad**:
1. **Confidentiality (Kerahasiaan):** Data sensitif (nilai ujian, password, data bank) hanya boleh dibaca oleh pemilik sah.
2. **Integrity (Keutuhan Data):** Data tidak boleh diubah, dirusak, atau dipalsukan di tengah jalan oleh pihak luar.
3. **Availability (Ketersediaan):** Sistem dan data harus selalu siap diakses saat dibutuhkan oleh pengguna resmi.

---

### 6.2. Jenis Ancaman & Metode Serangan Siber Populer

```
 ┌───────────────────┐    ┌────────────────────┐    ┌──────────────────────┐
 │     PHISHING      │    │     RANSOMWARE     │    │   MAN-IN-THE-MIDDLE  │
 │ Umpan link palsu  │    │  File dikunci dan  │    │ Menyadap data pada   │
 │ mencuri password  │    │  minta uang tebus  │    │ Wi-Fi publik palsu   │
 └───────────────────┘    └────────────────────┘    └──────────────────────┘
```

1. **Phishing (Pengelabuan):**
   - *Modus:* Pelaku mengirim email/pesan WhatsApp mengaku dari pihak resmi (bank, Instagram, kurir paket APK) yang mengarahkan korban ke formulir website palsu untuk mencuri username, password, dan PIN OTP.
2. **Malware & Ransomware (Perangkat Perusak & Pemeras):**
   - *Modus:* Virus jahat menginfeksi komputer korban (seringkali menyusup lewat software bajakan / game crack). **Ransomware** akan mengenkripsi (mengunci) seluruh dokumen korban dan meminta uang tebusan (ratusan juta rupiah) dalam bentuk Bitcoin untuk membuka kuncinya.
3. **Man-in-the-Middle (MitM) & Wi-Fi Rogue (Penyadapan Jalur):**
   - *Modus:* Hacker membuat hotspot Wi-Fi gratis tanpa password di kafe umum dengan nama mirip (*contoh: "Wi-Fi_Kafe_Gratis"*). Saat korban terhubung dan login ke web non-HTTPS, seluruh data password dan chat disadap secara real-time.
4. **DDoS Attack (*Distributed Denial of Service*):**
   - *Modus:* Membanjiri server website sekolah dengan jutaan permintaan palsu secara serentak dari ribuan komputer *botnet* hingga server kehabisan memori dan akhirnya *down/crash*.

---

### 6.3. Strategi Proteksi & Tata Kelola Keamanan Data

Bagaimana kita melindungi diri dan infrastruktur data sekolah?

1. **Keamanan Jaringan & Perimeter:**
   - **Firewall:** Dinding filter penyaring yang memblokir paket mencurigakan dan melarang akses port yang tidak diizinkan.
   - **Enkripsi HTTPS (SSL/TLS):** Pastikan alamat situs web memiliki ikon gembok (`https://`). Enkripsi mengubah teks sandi menjadi acak sehingga tidak bisa dibaca oleh penyadap Wi-Fi.
   - **Segmentasi Jaringan (VLAN):** Memisahkan jaringan Wi-Fi untuk tamu/siswa umum dari jaringan server keuangan sekolah.
2. **Tata Kelola Akses & Identitas (*Access Control*):**
   - **Prinsip Hak Akses Terkecil (*Principle of Least Privilege*):** Siswa hanya memiliki akses *Read* (membaca materi), guru memiliki hak *Edit/Write*, dan hanya administrator yang memiliki hak *Full Control*.
   - **MFA / 2FA (*Multi-Factor Authentication*):** Wajibkan autentikasi 2 langkah (Password + Notifikasi di HP/Aplikasi Authenticator).
   - **Manajemen Password yang Kuat:** Minimal 12 karakter kombinasi huruf besar, huruf kecil, angka, dan simbol (contoh: `Kucing#Lari89!`), serta tidak menggunakan password yang sama di semua platform.
3. **Penguatan Database & Backup Data:**
   - Database server harus selalu di-update (*patching security*), dienkripsi saat tersimpan (*Encryption at Rest*), dan menerapkan sistem pencadangan berkala (*3-2-1 Backup Strategy*: 3 salinan data, 2 media berbeda, 1 salinan disimpan di cloud/lokasi terpisah).

---

## BAB 7: Studi Kasus HOTS & Refleksi Kritis

Mari uji kemampuan analisis Anda sebagai calon arsitek jaringan dan pakar keamanan siber muda!

### 🔍 Kasus 1: Desain Infrastruktur Jaringan Laboratorium Baru
**Skenario:**  
SMA LABS baru saja membangun gedung laboratorium komputer 2 lantai.
- Lantai 1: 36 Komputer PC untuk Ujian CBT Nasional.
- Lantai 2: Ruang Guru (15 Laptop via Wi-Fi) dan Ruang Server Utama Sekolah.
- Anggaran sekolah mengutamakan keandalan tinggi (ujian CBT tidak boleh terputus jika satu kabel PC rusak) dan kemudahan penambahan komputer di masa depan.

**Tugas Analisis Anda:**
1. Topologi fisik apa yang paling tepat untuk 36 PC di Lantai 1? Jelaskan alasan logisnya!
2. Gambarkan alur perangkat keras dari sambungan kabel Fiber Optic ISP hingga sampai ke laptop guru dan PC siswa!
3. Perangkat keras apa saja yang harus dibeli? (Sebutkan Router, tipe Switch, Access Point, dan jenis kabel yang digunakan).

---

### 🔍 Kasus 2: Investigasi Insiden Kejahatan Siber di Sekolah
**Skenario:**  
Seorang siswa kelas X sedang mengerjakan tugas di kafe dekat sekolah menggunakan jaringan *"Free_Kafe_WiFi"*. Tiba-tiba akun media sosialnya diambil alih orang tak dikenal, dan file tugas di laptopnya berubah ekstensi menjadi `.locked` disertai pesan peringatan meminta uang tebusan Rp 5.000.000. Setelah ditelusuri, siswa tersebut 1 jam sebelumnya mengunduh software editor video "Full Crack Gratis" dari situs bajakan.

**Tugas Evaluasi Anda:**
1. Identifikasi dua jenis serangan siber yang menimpa siswa tersebut!
2. Mengapa terhubung ke Wi-Fi publik tanpa VPN/HTTPS sangat berbahaya?
3. Langkah pencegahan konkret apa saja yang seharusnya dilakukan siswa tersebut agar insiden serupa tidak terulang?

---

## Rangkuman Materi & Glosarium

### 📌 Intisari Materi
1. **Jaringan Komputer** memungkinkan pertukaran data dan pemanfaatan sumber daya secara bersama-sama.
2. Berdasarkan cakupan geografis, jaringan dibagi menjadi **PAN** (<10m), **LAN** (gedung/sekolah), **MAN** (kota), dan **WAN** (global/internet).
3. **Topologi Star** adalah standar industri saat ini untuk LAN karena memiliki keandalan tinggi dan isolasi gangguan yang baik.
4. **Router** menghubungkan jaringan yang berbeda subnet/internet, sedangkan **Switch** menghubungkan perangkat-perangkat lokal dalam satu subnet via MAC Address.
5. **Model OSI 7 Layer** dan **TCP/IP 4 Layer** adalah kerangka acuan standarisasi komunikasi data dari level kabel fisik hingga level aplikasi pengguna.
6. **Cyber Security** berfokus menjaga kerahasiaan (*Confidentiality*), keutuhan (*Integrity*), dan ketersediaan (*Availability*) data dari ancaman seperti Phishing, Ransomware, dan Penyadapan.

### 📚 Glosarium Istilah Penting
- **Bandwidth:** Kapasitas maksimal volume data yang dapat ditransfer melalui saluran komunikasi dalam satu detik (satuan Mbps/Gbps).
- **Latency (Ping):** Waktu tunda yang dibutuhkan sebuah paket data untuk menempuh perjalanan dari pengirim ke penerima dan kembali lagi (satuan milidetik / ms).
- **Packet:** Potongan kecil data terstandarisasi yang dikirimkan melintasi jaringan internet.
- **DNS (Domain Name System):** Penerjemah nama domain web menjadi alamat IP server tujuan.
- **DHCP:** Protokol otomatis pembagi alamat IP ke perangkat klien.
- **Firewall:** Sistem keamanan yang memonitor dan mengontrol lalu lintas jaringan masuk dan keluar berdasarkan aturan keamanan yang telah ditentukan.
- **Enkripsi:** Proses matematika mengubah teks biasa (*plaintext*) menjadi kode rahasia yang acak (*ciphertext*) agar tidak bisa dibaca oleh pihak yang tidak memiliki kunci dekripsi.
