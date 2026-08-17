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
