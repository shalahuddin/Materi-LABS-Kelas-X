# KUMPULAN CONTOH KODE PYTHON - ALGORITMA LANJUTAN (SEMESTER GENAP)
## Untuk Guru: Copy-paste ke Python IDE dan jalankan

---

## 1. MERGE SORT

```python
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
```

---

## 2. QUICK SORT

```python
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
```

---

## 3. REKURSI - FIBONACCI DENGAN MEMOIZATION

```python
def fibonacci_naive(n):
    """Naive recursion - SANGAT LAMBAT untuk n>40"""
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_memo(n, memo=None):
    """Memoization - CEPAT"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_tab(n):
    """Tabulation (iterative) - CEPAT & CLEAR"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Test & Bandingkan
print("\n=== FIBONACCI COMPARISON ===")
import time

n = 40
print(f"Menghitung fibonacci({n})...")

# Memo (cepat)
start = time.time()
result_memo = fibonacci_memo(n)
time_memo = time.time() - start
print(f"Memoization: {result_memo}, Time: {time_memo:.4f}s")

# Tabulation (cepat)
start = time.time()
result_tab = fibonacci_tab(n)
time_tab = time.time() - start
print(f"Tabulation: {result_tab}, Time: {time_tab:.4f}s")

# Naive (LAMBAT - skip jika tidak sabar)
# print("Naive: [SKIP - terlalu lambat]")
```

---

## 4. BFS & DFS GRAPH TRAVERSAL

```python
from collections import deque

def bfs(graph, start):
    """Breadth-First Search menggunakan queue"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def dfs(graph, start, visited=None):
    """Depth-First Search menggunakan recursion"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Test
print("\n=== BFS & DFS ===")
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print(f"BFS dari 0: {bfs(graph, 0)}")
print(f"DFS dari 0: {dfs(graph, 0)}")
```

---

## 5. DIJKSTRA'S ALGORITHM - SHORTEST PATH

```python
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm untuk shortest path.
    Kompleksitas: O((V+E) log V)
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Skip jika sudah processed
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Test
print("\n=== DIJKSTRA'S SHORTEST PATH ===")
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = dijkstra(graph, 'A')
print(f"Shortest distances dari A: {distances}")
print(f"A->A: {distances['A']}, A->B: {distances['B']}, A->C: {distances['C']}, A->D: {distances['D']}")
```

---

## 6. DYNAMIC PROGRAMMING - 0/1 KNAPSACK

```python
def knapsack(weights, values, capacity):
    """
    0/1 Knapsack problem dengan DP.
    Kompleksitas: O(n × capacity)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i-1][w]
            
            # Take item i-1 if possible
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i-1][w - weights[i-1]] + values[i-1]
                )
    
    return dp[n][capacity]

# Test
print("\n=== 0/1 KNAPSACK ===")
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack(weights, values, capacity)
print(f"Max value dengan capacity {capacity}: {max_value}")
```

---

## 7. BACKTRACKING - N-QUEENS SOLVER

```python
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
```

---

## 8. LONGEST COMMON SUBSEQUENCE (LCS)

```python
def lcs(s1, s2):
    """
    Longest Common Subsequence dengan DP.
    Kompleksitas: O(m × n)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Trace back LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], ''.join(reversed(lcs_str))

# Test
print("\n=== LONGEST COMMON SUBSEQUENCE ===")
s1, s2 = "ABCDGH", "AEDFHR"
length, lcs_string = lcs(s1, s2)
print(f"LCS({s1}, {s2}): {lcs_string} (panjang: {length})")
```

---

**Versi:** 1.0 | **Untuk:** Guru Informatika SMA Kelas X Semester Genap
