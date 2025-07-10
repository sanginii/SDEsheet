#tabulation
class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0]) 
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1]=grid[0][0]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    continue
                dp[i][j]=min(dp[i-1][j]+grid[i-1][j-1], dp[i][j-1]+grid[i-1][j-1])
        return dp[m][n] 

#memoization 
class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0]) 
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def memoization(i, j):
            if i<0 or j<0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[0][0]
            if dp[i][j]!= -1:
                return dp[i][j]
            dp[i][j]= grid[i][j] + min(memoization(i - 1, j), memoization(i, j - 1))
            return dp[i][j] 
        return memoization(m-1,n-1) 