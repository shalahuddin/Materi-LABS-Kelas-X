# MATERI PEMBELAJARAN DETAIL - ALGORITMA LANJUTAN (PART 2)
## Graph Algorithms, Backtracking, Dynamic Programming

---

## 4. BACKTRACKING (Minggu 7)

### Konsep
Backtracking adalah teknik recursif yang mengeksplorasi semua kemungkinan solusi dengan "mundur" jika solusi tidak valid.

**Karakteristik:**
- Recursion-based
- Explores all possibilities
- Prunes invalid branches early
- Kompleksitas: O(N!) worst case

### Template Backtracking
```
PROCEDURE Backtrack(candidate, solution)
  IF IsSolution(candidate) THEN
    AddToSolution(solution, candidate)
    RETURN
  END IF
  
  FOR each child IN GetChildren(candidate) DO
    IF IsValid(child) THEN
      Backtrack(child, solution)
    END IF
  END FOR
END PROCEDURE
```

### Contoh: N-Queens Problem
```python
def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    
    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            # Same column or diagonal
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

# Test: solve_n_queens(4) returns valid 4-queens solutions
```

### Aplikasi Backtracking
- Sudoku solver
- Maze solving
- Permutations & combinations
- Graph coloring
- Knight's tour

---

## 5. GRAPH ALGORITHMS (Minggu 8-11)

### 5A. Pengenalan Graph

**Terminologi:**
- **Vertex/Node:** Titik dalam graph
- **Edge:** Garis yang menghubungkan 2 vertex
- **Directed/Undirected:** Ada arah atau tidak
- **Weighted:** Setiap edge punya nilai (bobot)
- **Degree:** Jumlah edge yang terhubung ke vertex

**Representasi:**
```
1. Adjacency Matrix (matriks n×n)
   [0, 1, 0]
   [1, 0, 1]
   [0, 1, 0]

2. Adjacency List (dictionary/map)
   {0: [1], 1: [0, 2], 2: [1]}
```

### 5B. Breadth-First Search (BFS) — Minggu 9

**Konsep:** Jelajahi graph level-by-level menggunakan queue.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Test
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
print(bfs(graph, 0))  # [0, 1, 2, 3]
```

**Kompleksitas:** O(V + E) — V vertices, E edges

**Aplikasi:** Shortest path di unweighted graph, level-order traversal

### 5C. Depth-First Search (DFS) — Minggu 9

**Konsep:** Jelajahi graph sedalam mungkin menggunakan stack/recursion.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Test
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
print(dfs(graph, 0))  # [0, 1, 3, 2]
```

**Kompleksitas:** O(V + E)

**Aplikasi:** Topological sort, cycle detection, connected components

### 5D. Dijkstra's Algorithm (Minggu 11) — Shortest Path

**Konsep:** Menemukan jalur tersingkat dari source ke semua vertex dalam weighted graph.

**Pseudocode:**
```
ALGORITHM Dijkstra(graph, start)
  distance[start] = 0
  FOR each vertex v IN graph EXCEPT start:
    distance[v] = INFINITY
  END FOR
  
  unvisited = all vertices
  
  WHILE unvisited is not empty:
    current = vertex in unvisited dengan distance terkecil
    REMOVE current FROM unvisited
    
    FOR each neighbor OF current:
      alt_distance = distance[current] + weight(current, neighbor)
      IF alt_distance < distance[neighbor]:
        distance[neighbor] = alt_distance
      END IF
    END FOR
  END WHILE
  
  RETURN distance
END ALGORITHM
```

**Python Implementation:**
```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Test
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

**Kompleksitas:** O((V + E) log V) dengan min-heap

---

## 6. DYNAMIC PROGRAMMING (Minggu 12-13)

### Konsep Dasar
Dynamic Programming (DP) adalah teknik optimisasi yang menyimpan hasil subproblem yang sudah dihitung untuk menghindari rekomputasi.

**2 Karakteristik:**
1. **Optimal Substructure:** Solusi optimal terdiri dari solusi optimal subproblems
2. **Overlapping Subproblems:** Subproblems yang sama dihitung berkali-kali

**2 Pendekatan:**
1. **Memoization (Top-Down):** Recursion + caching
2. **Tabulation (Bottom-Up):** Iterative dengan table

### 6A. Fibonacci dengan DP

**Naive Recursion (Buruk):**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
# fib(40) sangat lambat — exponential!
```

**Memoization (Baik):**
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# fib_memo(40) instant — O(n)
```

**Tabulation (Juga Baik):**
```python
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# O(n) time, O(n) space
```

### 6B. 0/1 Knapsack Problem

**Problem:** Diberikan items dengan weight & value, pilih items yang maximize value dengan weight constraint.

**DP Approach:**
```python
def knapsack(weights, values, capacity):
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
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))  # 10 (items 0+3 atau 1+2)
```

**Kompleksitas:** O(n × capacity)

### 6C. Longest Common Subsequence (LCS)

**Problem:** Cari subsequence terpanjang yang common dari 2 strings.

```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Test
print(lcs("ABCDGH", "AEDFHR"))  # 3 (ADH)
```

**Aplikasi:** Diff tools, sequence alignment, longest increasing subsequence

---

**Versi:** 1.0 | **Untuk:** SMA Kelas X Algoritma Lanjutan (Semester Genap)
