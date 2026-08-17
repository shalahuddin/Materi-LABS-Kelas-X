def solve_n_queens(n):
    """
    N-Queens problem solver menggunakan backtracking.
    Kompleksitas: O(N!)
    """
    solutions = []
    board = [-1] * n
    
    def is_safe(row, col):
        """Check jika posisi col di row aman"""
        for prev_row in range(row):
            prev_col = board[prev_row]
            # Same column atau diagonal
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    backtrack(0)
    return solutions

# Test
print("\n=== N-QUEENS SOLVER ===")
for n in range(4, 6):
    solutions = solve_n_queens(n)
    print(f"{n}-Queens: {len(solutions)} solusi")
    if n == 4:
        print(f"  Solusi pertama: {solutions[0]}")
