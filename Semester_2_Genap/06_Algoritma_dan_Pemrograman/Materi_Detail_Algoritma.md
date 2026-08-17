# MATERI PEMBELAJARAN DETAIL - ALGORITMA DASAR

## 1. PENGERTIAN ALGORITMA

### Definisi
Algoritma adalah serangkaian langkah-langkah terurut dan terbatas untuk menyelesaikan suatu masalah.

**Karakteristik Algoritma:**
- **Terbatas (Finite):** Harus berakhir dalam jumlah langkah terbatas
- **Terurut (Ordered):** Langkah-langkah harus urut dan jelas
- **Definitif (Definite):** Setiap langkah harus jelas dan tidak ambigu
- **Efektif (Effective):** Setiap langkah dapat dilakukan

### Contoh Algoritma Sehari-hari
**Algoritma Membuat Teh:**
1. Ambil cangkir
2. Masukkan teh ke cangkir
3. Panaskan air hingga mendidih
4. Tuangkan air panas ke cangkir
5. Tunggu 3-5 menit
6. Aduk dan minum

---

## 2. REPRESENTASI ALGORITMA

### A. Pseudocode
Pseudocode adalah representasi algoritma menggunakan bahasa yang mirip bahasa pemrograman tapi lebih mudah dibaca.

**Contoh Pseudocode - Linear Search:**
```
ALGORITMA LinearSearch(array[], target)
  FOR i = 0 TO panjang(array) - 1 DO
    IF array[i] == target THEN
      RETURN i
    END IF
  END FOR
  RETURN -1  // tidak ditemukan
END ALGORITMA
```

### B. Flowchart
Flowchart adalah diagram yang menunjukkan alur algoritma menggunakan simbol-simbol khusus.

**Simbol Flowchart:**
- Oval: Start/End
- Rectangle: Process
- Diamond: Decision
- Parallelogram: Input/Output
- Arrow: Flow direction

---

## 3. ALGORITMA PENCARIAN (SEARCHING)

### A. Linear Search (Sequential Search)

**Konsep:** Memeriksa setiap elemen array dari awal hingga ditemukan atau sampai akhir.

**Pseudocode:**
```
FUNCTION LinearSearch(array[], n, target)
  FOR i = 0 TO n - 1 DO
    IF array[i] == target THEN
      RETURN i
    END IF
  END FOR
  RETURN -1  // tidak ditemukan
END FUNCTION
```

**Python Implementation:**
```python
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Test
arr = [5, 2, 8, 1, 9]
print(linear_search(arr, 8))  # Output: 2
print(linear_search(arr, 3))  # Output: -1
```

**Analisis Kompleksitas:**
- **Best Case:** O(1) - elemen ditemukan di posisi pertama
- **Average Case:** O(n) - elemen di tengah array
- **Worst Case:** O(n) - elemen tidak ada atau di posisi akhir

**Kelebihan:**
- Mudah dipahami dan diimplementasikan
- Bekerja pada array yang tidak terurut
- Tidak memerlukan memori tambahan

**Kekurangan:**
- Lambat untuk array besar
- Performa buruk pada worst case

**Kapan Digunakan:**
- Array kecil (< 1000 elemen)
- Data tidak terurut
- Pencarian pertama kali ditemukan saja

---

### B. Binary Search

**Prasyarat:** Data HARUS sudah terurut (sorted)

**Konsep:** Membagi array menjadi dua bagian, eliminasi bagian yang tidak perlu berdasarkan perbandingan dengan elemen tengah.

**Pseudocode:**
```
FUNCTION BinarySearch(array[], n, target)
  left = 0
  right = n - 1
  
  WHILE left <= right DO
    mid = (left + right) / 2
    
    IF array[mid] == target THEN
      RETURN mid
    ELSE IF array[mid] < target THEN
      left = mid + 1
    ELSE
      right = mid - 1
    END IF
  END WHILE
  
  RETURN -1
END FUNCTION
```

**Python Implementation:**
```python
def binary_search(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7))   # Output: 3
print(binary_search(arr, 10))  # Output: -1
```

**Analisis Kompleksitas:**
- **Best Case:** O(1)
- **Average Case:** O(log n)
- **Worst Case:** O(log n)

**Kelebihan:**
- Sangat cepat untuk data besar
- O(log n) jauh lebih baik dari O(n)
- Cocok untuk real-world applications

**Kekurangan:**
- Data harus terurut terlebih dahulu
- Hanya untuk array/sorted collections

**Contoh Eksekusi:**
```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Cari: 7

Iterasi 1: left=0, right=7, mid=3
  array[3]=7 ✓ DITEMUKAN di index 3
```

---

## 4. ALGORITMA PENGURUTAN (SORTING)

### A. Bubble Sort

**Konsep:** Membandingkan elemen berdekatan, tukar jika tidak sesuai urutan, ulangi hingga terurut.

**Pseudocode:**
```
PROCEDURE BubbleSort(array[], n)
  FOR i = 0 TO n - 1 DO
    FOR j = 0 TO n - i - 2 DO
      IF array[j] > array[j + 1] THEN
        SWAP(array[j], array[j + 1])
      END IF
    END FOR
  END FOR
END PROCEDURE
```

**Python Implementation:**
```python
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Test
arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))  # Output: [2, 3, 4, 5, 8]
```

**Analisis Kompleksitas:**
- **Best Case:** O(n) - array sudah terurut
- **Average Case:** O(n²)
- **Worst Case:** O(n²)
- **Space:** O(1) - in-place sorting

**Visualisasi (Pass 1-3):**
```
Pass 1: [5,3,4,2,8]
Pass 2: [3,4,2,5,8]
Pass 3: [3,2,4,5,8]
...
```

**Kelebihan:**
- Sangat mudah dipahami dan diimplementasikan
- Tidak perlu space tambahan (in-place)
- Stable sort

**Kekurangan:**
- Sangat lambat untuk data besar O(n²)
- Banyak perbandingan yang tidak perlu

**Kapan Digunakan:**
- Array sangat kecil (< 50 elemen)
- Pembelajaran/edukasi
- Data hampir terurut

---

### B. Selection Sort

**Konsep:** Menemukan elemen minimum, tempatkan di awal, ulangi dari sisa array.

**Python Implementation:**
```python
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
```

**Analisis Kompleksitas:**
- **Best/Average/Worst Case:** O(n²)
- **Space:** O(1)

---

### C. Insertion Sort

**Konsep:** Menempatkan elemen satu per satu ke posisi yang tepat di bagian terurut.

**Python Implementation:**
```python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
```

**Analisis Kompleksitas:**
- **Best Case:** O(n) - sudah terurut
- **Average Case:** O(n²)
- **Worst Case:** O(n²)
- **Space:** O(1)

---

## 5. ANALISIS KOMPLEKSITAS (BIG O NOTATION)

### Perbandingan Sorting Algorithms

| Algoritma | Best Case | Average | Worst Case | Space | Stable |
|-----------|-----------|---------|-----------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Ya |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | Tidak |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Ya |

### Kapan Gunakan Algoritma Mana?

- **Linear Search:** Data kecil, tidak terurut
- **Binary Search:** Data besar, terurut
- **Bubble Sort:** Edukasi, data sangat kecil
- **Selection Sort:** Edukasi, data kecil
- **Insertion Sort:** Data kecil-menengah, hampir terurut

---

## 6. PSEUDOCODE vs CODE COMPARISON

### Contoh: Linear Search

**Pseudocode:**
```
FUNCTION Search(array[], n, x)
  FOR i = 0 TO n - 1 DO
    IF array[i] == x THEN
      RETURN i
    END IF
  END FOR
  RETURN -1
END FUNCTION
```

**Python Code:**
```python
def search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1
```

**Java Code:**
```java
public static int search(int[] array, int x) {
    for (int i = 0; i < array.length; i++) {
        if (array[i] == x) {
            return i;
        }
    }
    return -1;
}
```

---

## 7. AKTIVITAS PEMBELAJARAN

### Aktivitas 1: Manual Trace (Minggu 6)
**Tujuan:** Memahami step-by-step linear search

**Instruksi:**
1. Diberikan array: [3, 7, 1, 9, 5, 2]
2. Cari element: 9
3. Trace manual:
   - i=0: array[0]=3, tidak sama
   - i=1: array[1]=7, tidak sama
   - i=2: array[2]=1, tidak sama
   - i=3: array[3]=9, DITEMUKAN ✓
4. Output: index 3

### Aktivitas 2: Simulasi Sorting (Minggu 8)
**Alat:** Kartu bertulisan angka atau objek fisik

**Prosedur:**
1. Siswa disusun dengan kartu angka di dada
2. Simulasikan bubble sort: bandingkan berdekatan, tukar jika perlu
3. Ulangi pass sampai terurut
4. Diskusi: berapa pass yang dibutuhkan?

### Aktivitas 3: Kode Aktual (Minggu 12)
**Instruksi:**
1. Buka Python IDE
2. Ketik linear_search function
3. Test dengan berbagai input
4. Modifikasi untuk binary_search
5. Bandingkan waktu eksekusi

---

## 8. SOAL LATIHAN

### Level 1: Pemahaman Konsep

**1. Definisi Algoritma**
Jelaskan apa itu algoritma dengan bahasa sendiri dan berikan contoh dari kehidupan sehari-hari.

**2. Perbedaan Linear vs Binary Search**
- Kapan menggunakan linear search?
- Kapan menggunakan binary search?
- Apa prasyarat binary search?

**3. Kompleksitas Big O**
Urutkan dari cepat ke lambat: O(n²), O(1), O(n), O(log n)

### Level 2: Implementasi Kode

**1. Linear Search**
Implementasikan linear_search dalam Python. Test dengan 3 test cases.

**2. Bubble Sort**
Implementasikan bubble_sort. Trace untuk array [5, 2, 8, 1].

**3. Kompleksitas Analisis**
Berapa kompleksitas worst case untuk array besar n=1000000?

### Level 3: Problem Solving

**1. Modifikasi Algoritma**
Modifikasi binary_search untuk mengembalikan semua posisi jika ada duplicate.

**2. Pilih Algoritma Terbaik**
Diberikan 100,000 data terurut. Pilih search algorithm. Jelaskan alasan.

---

**Versi:** 1.0 | **Untuk:** SMA Kelas X Algoritma | **Tanggal:** 19 Juli 2026
