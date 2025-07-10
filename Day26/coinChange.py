#memoization
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [-1]*(amount+1)
        def solve(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if dp[amt]!=-1:
                return dp[amt] 
            min_coins = float('inf')
            for coin in coins:
                res = solve(amt - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)
            dp[amt] = min_coins
            return dp[amt]
        ans = solve(amount)
        return ans if ans != float('inf') else -1
    
#tabulation
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1, amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i] = min (dp[i], 1 + dp[i-coin]) 
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
            