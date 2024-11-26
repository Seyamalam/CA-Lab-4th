def knapsack(items, W):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1][0] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], items[i - 1][1] + dp[i - 1][w - items[i - 1][0]])
    return dp[n][W]


items = [(10, 60), (20, 100), (30, 120)]
W = 50
print(f"Maximum value: {knapsack(items, W)}")
