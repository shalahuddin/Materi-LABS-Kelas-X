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
