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
