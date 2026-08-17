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
