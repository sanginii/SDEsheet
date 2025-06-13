#bruteforce using recursion
n=2 #rows
m=3 #columns
#cannot use global variables
def grid(i, j):
    if i==n-1 and j==m-1:
        return 1
    if i>=n or j>=m:
        return 0
    paths = grid(i+1,j) + grid(i,j+1) 
    return (paths)
print (grid(0,0))

#self is instance of class so we are using class or self we have to use the other 
#using dynamic programming
def grid(i, j, dp):
    if i==n-1 and j==m-1:
        return 1
    if i>=n or j>=m:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    else:
        dp[i][j] =  grid(i+1,j,dp) + grid(i,j+1,dp)
        return dp[i][j]

dp = [[-1]*m for _ in range(n)]
print (grid(0,0,dp)) 