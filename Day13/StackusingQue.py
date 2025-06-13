from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, data):
        self.q.append(data)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())  # rotate to bring new item to front

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.q.popleft()  # top of stack is always at front

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

# Example usage
s = StackUsingQueue()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())   # 30
print(s.top())   # 20
