#recursive
def knapsack(weights, values, n, W):
    # Base case: no items or no capacity
    if n == 0 or W == 0:
        return 0
    
    # If weight of nth item is more than capacity, skip it
    if weights[n-1] > W:
        return knapsack(weights, values, n-1, W)
    
    # Max of two cases:
    # (1) nth item included
    # (2) not included
    include = values[n-1] + knapsack(weights, values, n-1, W - weights[n-1])
    exclude = knapsack(weights, values, n-1, W)
    
    return max(include, exclude)

#tabulation bottom-up iterative
def knapsack(weights, values, n, W):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                include = values[i-1] + dp[i-1][w - weights[i-1]]
                exclude = dp[i-1][w]
                dp[i][w] = max(include, exclude)
    
    return dp[n][W]

weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
W = 8
n = len(weights)

print(knapsack(weights, values, n, W))  # Output: 110 

#memoization top-down recursive
def knapsack(weights, values, n, W, dp):
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]#important
    
    if weights[n-1] > W:
        dp[n][W] = knapsack(weights, values, n-1, W, dp)
    else:
        include = values[n-1] + knapsack(weights, values, n-1, W - weights[n-1], dp)
        exclude = knapsack(weights, values, n-1, W, dp)
        dp[n][W] = max(include, exclude)
    
    return dp[n][W]

n = len(weights)
dp = [[-1 for _ in range(W+1)] for _ in range(n+1)]
knapsack(weights, values, n, W, dp)