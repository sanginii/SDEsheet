#memoization
def matrix_chain_multiplication(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def solve(i, j):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        min_cost = float('inf')

        for k in range(i, j):
            cost = (solve(i, k) +
                    solve(k + 1, j) +
                    arr[i - 1] * arr[k] * arr[j])
            min_cost = min(min_cost, cost)

        dp[i][j] = min_cost
        return dp[i][j]

    return solve(1, n - 1) 

#tabulation
import sys

def matrix_chain_multiplication(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):  # chain length from 2 to n-1
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        arr[i - 1] * arr[k] * arr[j])
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n - 1]
