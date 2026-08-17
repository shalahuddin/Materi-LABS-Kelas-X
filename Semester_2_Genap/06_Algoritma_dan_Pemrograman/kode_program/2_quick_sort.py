def quick_sort(array, low=0, high=None):
    """
    Quick Sort dengan divide & conquer.
    Kompleksitas: O(n log n) average, O(n²) worst
    Space: O(log n) untuk recursion stack
    """
    if high is None:
        high = len(array) - 1
    
    if low < high:
        pivot_idx = partition(array, low, high)
        quick_sort(array, low, pivot_idx - 1)
        quick_sort(array, pivot_idx + 1, high)
    
    return array

def partition(array, low, high):
    """Partition array dengan pivot"""
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Contoh penggunaan
print("\n=== QUICK SORT ===")
numbers = [5, 2, 8, 1, 9, 3, 7]
print(f"Array sebelum: {numbers}")
print(f"Array sesudah: {quick_sort(numbers.copy())}")
