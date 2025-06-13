class Stack:
    def __init__ (self):
        self.s = []
    def is_empty(self):
        return len(self.s)==0
    def push (self, data):
        self.s.append(data)
    def pop (self):
        if self.is_empty():
            return "Stack is empty"
        return self.s.pop()
    def print (self):
        print (self.s)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(20) 
print (s.pop())
s.print()
