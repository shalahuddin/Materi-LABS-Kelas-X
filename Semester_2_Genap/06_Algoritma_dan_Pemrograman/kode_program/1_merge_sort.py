def merge_sort(array):
    """
    Merge Sort menggunakan divide & conquer.
    Kompleksitas: O(n log n) untuk semua kasus
    Space: O(n)
    """
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge 2 sorted arrays"""
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

# Contoh penggunaan
print("=== MERGE SORT ===")
numbers = [5, 2, 8, 1, 9, 3, 7]
print(f"Array sebelum: {numbers}")
print(f"Array sesudah: {merge_sort(numbers)}")
