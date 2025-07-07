import heapq
class Solution:
    def kth_Largest_MaxHeap(self, arr, k):
        pq = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(pq, -arr[i])
        f = k - 1
        while f > 0:
            heapq.heappop(pq)
            f -= 1
        print("Kth Largest element", -pq[0])

    def kth_Smallest_MinHeap(self, arr, k):
        pq = []
        n = len(arr)
        for i in range(n):
            heapq.heappush(pq, arr[i])
        f = k - 1
        while f > 0:
            heapq.heappop(pq)
            f -= 1
        print("Kth Smallest element", pq[0])
if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]
    obj = Solution()
    obj.kth_Largest_MaxHeap(arr, 3)
    obj.kth_Smallest_MinHeap(arr, 3) 
