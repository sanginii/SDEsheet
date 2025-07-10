class Solution:
    def maxSumIS(self, nums) -> int:
        n = len(nums)
        dp = nums[:]  # dp[i] = max sum ending at index i

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + nums[i])

        return max(dp)
