# KUMPULAN CONTOH KODE PYTHON - ALGORITMA DASAR
## Untuk Guru: Copy-paste ke Python IDE dan jalankan

---

## 1. LINEAR SEARCH

```python
def linear_search(array, target):
    """
    Mencari elemen target dalam array menggunakan linear search.
    Return: index jika ditemukan, -1 jika tidak ditemukan
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Contoh penggunaan
print("=== LINEAR SEARCH ===")
numbers = [5, 2, 8, 1, 9, 3, 7]
print(f"Array: {numbers}")
print(f"Cari 9: index {linear_search(numbers, 9)}")  # Output: 4
print(f"Cari 10: index {linear_search(numbers, 10)}")  # Output: -1
```

---

## 2. BINARY SEARCH

```python
def binary_search(array, target):
    """
    Mencari elemen target dalam SORTED array menggunakan binary search.
    PENTING: Array HARUS sudah terurut!
    Return: index jika ditemukan, -1 jika tidak
    """
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

# Contoh penggunaan
print("\n=== BINARY SEARCH ===")
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Array terurut: {sorted_numbers}")
print(f"Cari 7: index {binary_search(sorted_numbers, 7)}")  # Output: 3
print(f"Cari 10: index {binary_search(sorted_numbers, 10)}")  # Output: -1
```

---

## 3. BUBBLE SORT

```python
def bubble_sort(array):
    """
    Mengurutkan array menggunakan bubble sort (ascending).
    Kompleksitas: O(n²) worst case
    """
    n = len(array)
    
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # Tukar elemen
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        
        # Optimasi: jika tidak ada swap, array sudah terurut
        if not swapped:
            break
    
    return array

# Contoh penggunaan
print("\n=== BUBBLE SORT ===")
numbers = [5, 2, 8, 1, 9, 3]
print(f"Array sebelum sort: {numbers}")
result = bubble_sort(numbers.copy())
print(f"Array sesudah sort: {result}")
```

---

## 4. SELECTION SORT

```python
def selection_sort(array):
    """
    Mengurutkan array menggunakan selection sort (ascending).
    Kompleksitas: O(n²) untuk semua kasus
    """
    n = len(array)
    
    for i in range(n):
        # Cari index minimum dari sisa array
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        
        # Tukar dengan elemen di posisi i
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

# Contoh penggunaan
print("\n=== SELECTION SORT ===")
numbers = [5, 2, 8, 1, 9, 3]
print(f"Array sebelum sort: {numbers}")
result = selection_sort(numbers.copy())
print(f"Array sesudah sort: {result}")
```

---

## 5. INSERTION SORT

```python
def insertion_sort(array):
    """
    Mengurutkan array menggunakan insertion sort (ascending).
    Kompleksitas: O(n) best case, O(n²) worst case
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        # Geser elemen yang lebih besar ke kanan
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key
    
    return array

# Contoh penggunaan
print("\n=== INSERTION SORT ===")
numbers = [5, 2, 8, 1, 9, 3]
print(f"Array sebelum sort: {numbers}")
result = insertion_sort(numbers.copy())
print(f"Array sesudah sort: {result}")
```

---

## 6. PROGRAM INTERAKTIF - SEARCHING & SORTING

```python
def menu_searching():
    """Menu untuk testing searching algorithms"""
    print("\n=== TESTING SEARCHING ALGORITHMS ===")
    array = [5, 2, 8, 1, 9, 3, 7]
    print(f"Array: {array}")
    target = int(input("Masukkan angka yang dicari: "))
    
    result = linear_search(array, target)
    if result != -1:
        print(f"✓ Ditemukan di index {result}")
    else:
        print(f"✗ Tidak ditemukan")

def menu_sorting():
    """Menu untuk testing sorting algorithms"""
    print("\n=== TESTING SORTING ALGORITHMS ===")
    array = [5, 2, 8, 1, 9, 3, 7]
    print(f"Array original: {array}")
    
    print("\nPilih algoritma sorting:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    
    choice = input("Masukkan pilihan (1-3): ")
    
    if choice == "1":
        result = bubble_sort(array.copy())
        print(f"Hasil Bubble Sort: {result}")
    elif choice == "2":
        result = selection_sort(array.copy())
        print(f"Hasil Selection Sort: {result}")
    elif choice == "3":
        result = insertion_sort(array.copy())
        print(f"Hasil Insertion Sort: {result}")

# Main program
if __name__ == "__main__":
    while True:
        print("\n" + "="*40)
        print("PROGRAM PEMBELAJARAN ALGORITMA")
        print("="*40)
        print("1. Test Searching")
        print("2. Test Sorting")
        print("3. Keluar")
        
        menu = input("Pilih menu (1-3): ")
        
        if menu == "1":
            menu_searching()
        elif menu == "2":
            menu_sorting()
        elif menu == "3":
            print("Terima kasih! Goodbye!")
            break
        else:
            print("Pilihan tidak valid!")
```

---

## CATATAN UNTUK GURU:
- Copy kode di atas ke Python IDE
- Jalankan dan tunjukkan output kepada siswa
- Modifikasi array test untuk berbagai skenario
- Minta siswa trace manual sebelum menjalankan
- Bandingkan output antar algoritma

**Versi:** 1.0 | **Untuk:** Guru Informatika SMA Kelas X
