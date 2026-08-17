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
