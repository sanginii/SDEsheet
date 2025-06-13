class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Main stack
        self.stack2 = []  # Helper stack

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        # Move all elements to stack2 to reverse the order
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Pop the front of queue (top of stack2)
        result = self.stack2.pop()

        # Move elements back to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return result

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        result = self.stack2[-1]

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return result

    def is_empty(self):
        return len(self.stack1) == 0

    def size(self):
        return len(self.stack1)

# Example usage
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # 10
print(q.peek())     # 20
print(q.size())     # 2
