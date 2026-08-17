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
