class Solution:
    def maxProduct(self, nums) -> int:
        res = max(nums)
        curr_max,curr_min = 1,1
        for i in nums:
            if i==0:
                curr_max,curr_min = 1,1
                continue
            tmp = curr_max*i
            curr_max = max(curr_max*i, curr_min*i, i)
            curr_min = min(tmp, curr_min*i, i) 
            res = max(res, curr_max)
        return res