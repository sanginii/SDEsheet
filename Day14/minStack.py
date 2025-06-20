class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # Keeps track of current minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val <= current min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # If the popped value is the current min, pop from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
