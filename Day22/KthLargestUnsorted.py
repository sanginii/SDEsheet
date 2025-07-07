import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            if i < self.k:
                heapq.heappush(self.heap, nums[i])
            if i >= self.k and nums[i]>self.heap[0]:
                heapq.heappop(self.heap) 
                heapq.heappush(self.heap, nums[i]) 

    def add(self, val: int) -> int:
        if len(self.heap) == self.k and val>self.heap[0]:
            heapq.heappop(self.heap) 
            heapq.heappush(self.heap, val) 
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        return self.heap[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)