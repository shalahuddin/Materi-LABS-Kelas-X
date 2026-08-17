# MATERI PEMBELAJARAN DETAIL - ALGORITMA LANJUTAN
## Semester Genap: Merge Sort, Quick Sort, Rekursi, Graph, Dynamic Programming

---

## 1. MERGE SORT (Minggu 2)

### Konsep: Divide & Conquer
Merge Sort membagi array menjadi 2 bagian, sort masing-masing, kemudian merge kembali.

**Karakteristik:**
- **Strategi:** Divide-and-Conquer
- **Kompleksitas:** O(n log n) untuk semua kasus (best, average, worst)
- **Space:** O(n) - memerlukan space tambahan
- **Stable:** Ya - urutan elemen yang sama tetap terjaga

### Pseudocode
```
PROCEDURE MergeSort(array[], left, right)
  IF left < right THEN
    mid = (left + right) / 2
    MergeSort(array, left, mid)
    MergeSort(array, mid+1, right)
    Merge(array, left, mid, right)
  END IF
END PROCEDURE

PROCEDURE Merge(array[], left, mid, right)
  left_arr = array[left...mid]
  right_arr = array[mid+1...right]
  i = 0, j = 0, k = left
  
  WHILE i < length(left_arr) AND j < length(right_arr) DO
    IF left_arr[i] <= right_arr[j] THEN
      array[k] = left_arr[i]
      i = i + 1
    ELSE
      array[k] = right_arr[j]
      j = j + 1
    END IF
    k = k + 1
  END WHILE
  
  // Copy sisa elemen
  WHILE i < length(left_arr) DO
    array[k] = left_arr[i]
    i = i + 1
    k = k + 1
  END WHILE
  
  WHILE j < length(right_arr) DO
    array[k] = right_arr[j]
    j = j + 1
    k = k + 1
  END WHILE
END PROCEDURE
```

### Python Implementation
```python
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
arr = [5, 2, 8, 1, 9]
print(merge_sort(arr))  # [1, 2, 5, 8, 9]
```

### Kelebihan & Kekurangan
✅ Kelebihan:
- O(n log n) guaranteed (predictable performa)
- Stable sort
- Baik untuk linked lists
- Parallelizable

❌ Kekurangan:
- Memerlukan O(n) space tambahan
- Overhead rekursi
- Lebih lambat dari quicksort pada praktik untuk array kecil

### Kapan Digunakan
- Data besar dengan performa konsisten diperlukan
- Linked lists
- External sorting (data tidak muat di memory)
- Stable sort diperlukan

---

## 2. QUICK SORT (Minggu 3)

### Konsep: Divide & Conquer dengan Partisioning
Quick Sort memilih pivot, partisi array, lalu sort sub-arrays secara rekursif.

**Karakteristik:**
- **Strategi:** Divide-and-Conquer
- **Kompleksitas:** 
  - Best/Average: O(n log n)
  - Worst: O(n²) - jika pivot selalu ekstrem
- **Space:** O(log n) - rekursi stack
- **Stable:** Tidak (tapi bisa dimodifikasi)

### Pseudocode
```
PROCEDURE QuickSort(array[], low, high)
  IF low < high THEN
    pivot_idx = Partition(array, low, high)
    QuickSort(array, low, pivot_idx - 1)
    QuickSort(array, pivot_idx + 1, high)
  END IF
END PROCEDURE

PROCEDURE Partition(array[], low, high)
  pivot = array[high]
  i = low - 1
  
  FOR j = low TO high - 1 DO
    IF array[j] < pivot THEN
      i = i + 1
      SWAP(array[i], array[j])
    END IF
  END FOR
  
  SWAP(array[i + 1], array[high])
  RETURN i + 1
END PROCEDURE
```

### Python Implementation
```python
def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    
    if low < high:
        pivot_idx = partition(array, low, high)
        quick_sort(array, low, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, high)
    
    return array

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Test
arr = [5, 2, 8, 1, 9]
print(quick_sort(arr))  # [1, 2, 5, 8, 9]
```

### Pivot Selection Strategies
- **Last element:** Sederhana tapi tidak optimal
- **First element:** Sama dengan last
- **Middle element:** Lebih baik
- **Random element:** Hindari worst case
- **Median-of-three:** Kombinasi baik

### Kelebihan & Kekurangan
✅ Kelebihan:
- Fast pada praktik (cache-friendly)
- O(log n) space
- In-place sorting
- Dapat parallelized

❌ Kekurangan:
- Worst case O(n²)
- Tidak stable
- Rekursi (call stack)

### Kapan Digunakan
- General-purpose sorting (default untuk banyak library)
- Ketika average case O(n log n) cukup baik
- Memory terbatas (in-place)
- Randomized pivot untuk menghindari worst case

---

## 3. REKURSI (Minggu 6-7)

### Konsep Dasar
Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri.

**Komponen Rekursi:**
1. **Base Case:** Kondisi stop rekursi
2. **Recursive Case:** Fungsi memanggil dirinya
3. **Progress toward base case:** Setiap call lebih dekat ke base case

### Contoh: Factorial
```
FUNCTION Factorial(n)
  IF n == 0 OR n == 1 THEN
    RETURN 1  // Base case
  ELSE
    RETURN n * Factorial(n - 1)  // Recursive case
  END IF
END FUNCTION
```

### Python Implementation
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

# Test
print(factorial(5))  # 5*4*3*2*1 = 120
```

### Kompleksitas Rekursi
- **Time:** Bergantung pada jumlah call dan work per call
- **Space:** Call stack depth

### Masalah: Stack Overflow
Rekursi yang dalam menyebabkan stack overflow. Solusi:
- Tail recursion optimization (tidak semua bahasa support)
- Iterative approach
- Memoization untuk mengurangi calls

