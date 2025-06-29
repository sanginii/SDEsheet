class Solution:
    def singleNonDuplicate(self, nums) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even to compare with next
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]
