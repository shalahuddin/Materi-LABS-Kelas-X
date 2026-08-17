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
