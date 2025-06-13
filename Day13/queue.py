class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)  # Insert at end

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)  # Remove from front

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue (front -> rear):", self.queue)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:", q.dequeue())
print("Front element:", q.peek())
print("Queue size:", q.size())


# collections.deque
# queue.Queue
# queue.LifoQueue 