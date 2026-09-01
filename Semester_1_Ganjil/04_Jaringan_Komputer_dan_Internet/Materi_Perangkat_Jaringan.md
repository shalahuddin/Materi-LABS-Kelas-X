---
name: perangkat-jaringan
description: Pengetahuan dasar tentang perangkat jaringan seperti Access Point, Switch, LAN, Router, Hub, dan lain‑lain untuk siswa SMA.
metadata:
  type: user
---
# Pengetahuan Perangkat Jaringan

## 1. LAN (Local Area Network)
- **Definisi:** Jaringan yang menghubungkan perangkat‑perangkat dalam area geografis kecil (mis. kelas, laboratorium, rumah). 
- **Ciri‑ciri:** Kecepatan tinggi (biasanya 100 Mbps – 10 Gbps), latensi rendah, biasanya menggunakan kabel **Ethernet** atau **Wi‑Fi**.
- **Contoh penggunaan:**
  - Komputer di lab harus terhubung ke server file.
  - Siswa mengakses printer bersama di kelas.

## 2. Switch (Ethernet Switch)
- **Fungsi utama:** Menghubungkan banyak perangkat dalam satu LAN dan **mengirim paket data** hanya ke perangkat tujuan (menggunakan **MAC address**).
- **Cara kerja sederhana:** Setiap port pada switch memiliki tabel MAC yang mencatat alamat perangkat yang terhubung; ketika paket datang, switch mengirimkannya ke port yang tepat.
- **Keuntungan dibanding hub:**
  - **Segmentasi**: Hanya perangkat tujuan yang menerima data, mengurangi tabrakan.
  - **Kecepatan**: Full‑duplex (dua arah sekaligus).
- **Jenis switch:**
  - **Unmanaged:** Plug‑and‑play, tidak dapat dikonfigurasi.
  - **Managed:** Dapat di‑configurasi (VLAN, QoS) – biasanya dipakai di jaringan sekolah atau kantor.

## 3. Access Point (AP)
- **Definisi:** Perangkat yang **menyediakan jaringan Wi‑Fi** dengan menghubungkan perangkat nirkabel ke jaringan kabel (biasanya ke switch).
- **Perbedaan dengan router wireless:**
  - **AP** hanya menambah kemampuan nirkabel pada jaringan yang sudah ada (tidak mengatur IP).
  - **Router wireless** biasanya memiliki fungsi routing (menghubungkan jaringan berbeda) sekaligus AP.
- **Fitur penting pada AP:**
  - **SSID** (nama jaringan) yang dapat disembunyikan atau dipublikasikan.
  - **Channel**: Frekuensi yang digunakan (2.4 GHz atau 5 GHz). Pilih channel yang tidak bentrok dengan AP lain.
  - **Keamanan:** WPA2‑PSK atau WPA3, enkripsi data.
- **Kegunaan dalam kelas:** Siswa dapat mengakses internet via laptop/tablet tanpa kabel.

## 4. Router
- **Fungsi utama:** Menghubungkan **dua jaringan yang berbeda** (mis. LAN sekolah dengan internet). 
- **Komponen dasar:**
  - **Interface WAN:** Terhubung ke ISP (Internet Service Provider).
  - **Interface LAN:** Terhubung ke switch atau AP untuk jaringan internal.
  - **Routing Table:** Menentukan jalur paket antara jaringan.
- **Fitur tambahan (umum pada router sekolah):**
  - **NAT (Network Address Translation):** Mengubah alamat IP internal menjadi satu alamat publik.
  - **DHCP Server:** Memberi alamat IP otomatis ke perangkat yang terhubung.
  - **Firewall:** Menyaring paket berbahaya.

## 5. Hub (Ethernet Hub) – Sejarah singkat
- **Definisi:** Perangkat jaringan yang **mengirimkan** setiap paket yang diterima ke **semua** port lain.
- **Kelemahan:** Banyak **tabrakan** (collision) karena semua perangkat berbagi satu saluran.
- **Penggunaan saat ini:** Sangat jarang; hampir seluruh jaringan modern memakai **switch**.

## 6. Modem (Modulator‑Demodulator)
- **Fungsi:** Mengubah sinyal digital dari komputer menjadi sinyal analog yang dapat dikirim melalui saluran telepon/kabel, dan sebaliknya.
- **Jenis:**
  - **DSL Modem, Cable Modem, Fiber ONT** – tergantung jenis layanan ISP.
- **Koneksi ke router:** Modem biasanya terhubung ke **WAN port** router untuk memberikan akses internet.

## 7. NIC (Network Interface Card)
- **Definisi:** Kartu atau modul yang memberikan **interface** jaringan ke komputer (Ethernet atau Wi‑Fi).
- **Komponen penting:**
  - **MAC address** unik tiap NIC.
  - **Port Ethernet RJ‑45** (untuk kabel) atau **antena Wi‑Fi**.
- **Penggunaan:** Semua komputer, laptop, atau Raspberry Pi membutuhkan NIC untuk bergabung ke jaringan.

## 8. Contoh Topologi Sederhana di Sekolah
```
[Modem] → [Router] → [Switch] → [PC 1]
                       ↘︎ [PC 2]
                       ↘︎ [AP] → [Laptop Wi‑Fi]
```
- **Modem** menghubungkan jaringan sekolah ke internet.
- **Router** mengatur lalu lintas antara jaringan internal dan internet.
- **Switch** menyebarkan koneksi kabel ke beberapa PC.
- **AP** memberi akses nirkabel ke perangkat mobile.

## 9. Pertanyaan Refleksi (untuk siswa)
1. Mengapa **switch** lebih efisien daripada **hub** dalam sebuah LAN?
2. Apa peran **MAC address** pada switch?
3. Bagaimana **router** dapat menghubungkan jaringan lokal dengan internet?
4. Sebutkan dua perbedaan utama antara **Access Point** dan **Router Wireless**.
5. Mengapa keamanan (WPA2/WPA3) penting pada **AP** di lingkungan sekolah?

---
*Materi ini dapat dipadukan ke dalam RPP atau lembar aktivitas untuk memberi siswa gambaran lengkap tentang perangkat‑perangkat jaringan yang umum ditemui di sekolah.*
