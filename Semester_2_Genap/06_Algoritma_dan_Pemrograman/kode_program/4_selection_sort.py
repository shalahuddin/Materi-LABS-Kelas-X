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
