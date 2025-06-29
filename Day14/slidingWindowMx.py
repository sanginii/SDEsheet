from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for i in range(len(nums)):
            # Remove all indices whose corresponding values are less than nums[i]
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)

            # Remove indices that are out of this window
            if queue[0] <= i - k:
                queue.popleft()

            # Add to answer once the first window is fully traversed
            if i >= k - 1:
                ans.append(nums[queue[0]])
        
        return ans
