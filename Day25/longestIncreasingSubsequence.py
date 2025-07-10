#N^2
class Solution:
    def lengthOfLIS(self, nums) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums),-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i], 1+LIS[j]) 
        return max(LIS)
import bisect
#binary search
def lengthOfLIS(self, nums) -> int:
        temp = [nums[0]]
        for i in range(len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                ind = bisect.bisect_left(temp, nums[i])
                temp[ind]=nums[i]
        return len(temp)