#whenever asked in k terms heaps can be used
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build frequency map manually
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Step 2: Use min-heap to keep top k frequent elements
        heap = []  # (frequency, num)
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract just the elements from heap
        return [num for freq, num in heap]
