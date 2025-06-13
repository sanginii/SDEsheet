class Solution:
    def initializeHeap(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def changeKey(self, index, new_val):
        old_val = self.heap[index]
        self.heap[index] = new_val
        if new_val > old_val:
            self._heapify_up(index)
        else:
            self._heapify_down(index)

    def extractMax(self):
        if self.isEmpty():
            return None
        max_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return max_val

    def isEmpty(self):
        return len(self.heap) == 0

    def getMax(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def heapSize(self):
        return len(self.heap)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
