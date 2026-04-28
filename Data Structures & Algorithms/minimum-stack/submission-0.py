class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []  # tracks current min at each push

    def push(self, val):
        self.stack.append(val)
        # min is either val or whatever the current min is
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()  # discard the min for that level too

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]