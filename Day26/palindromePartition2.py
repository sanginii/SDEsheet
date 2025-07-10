class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        
        # Precompute palindrome substrings
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_palindrome[i+1][j-1]):
                    is_palindrome[i][j] = True

        def min_cuts(i):
            if i == n:
                return 0  # No cuts needed after end
            if dp[i] != -1:
                return dp[i]
            
            min_cut = float('inf')
            for j in range(i, n):
                if is_palindrome[i][j]:
                    cuts = 1 + min_cuts(j + 1)  # 1 cut before this partition
                    min_cut = min(min_cut, cuts)
            
            dp[i] = min_cut
            return dp[i]
        
        return min_cuts(0) - 1  # Subtract 1 because the last partition doesn’t need a cut
