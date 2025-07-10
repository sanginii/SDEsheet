#memoization
def eggDrop(k, n):
    dp = [[-1] * (n + 1) for _ in range(k + 1)]

    def solve(k, n):
        if n == 0 or n == 1:
            return n
        if k == 1:
            return n
        if dp[k][n] != -1:
            return dp[k][n]

        min_attempts = float('inf')

        # Binary search optimization
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            break_case = solve(k - 1, mid - 1)
            no_break_case = solve(k, n - mid)
            worst_case = 1 + max(break_case, no_break_case)

            if break_case > no_break_case:
                high = mid - 1
            else:
                low = mid + 1

            min_attempts = min(min_attempts, worst_case)

        dp[k][n] = min_attempts
        return dp[k][n]

    return solve(k, n)
#tabulation
def eggDrop(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base case: 0 floors -> 0 attempts, 1 floor -> 1 attempt
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1

    for j in range(1, n + 1):
        dp[1][j] = j

    for eggs in range(2, k + 1):
        for floors in range(2, n + 1):
            low, high = 1, floors
            ans = float('inf')
            while low <= high:
                mid = (low + high) // 2
                break_case = dp[eggs - 1][mid - 1]
                no_break_case = dp[eggs][floors - mid]
                worst = 1 + max(break_case, no_break_case)

                if break_case > no_break_case:
                    high = mid - 1
                else:
                    low = mid + 1

                ans = min(ans, worst)
            dp[eggs][floors] = ans

    return dp[k][n]
