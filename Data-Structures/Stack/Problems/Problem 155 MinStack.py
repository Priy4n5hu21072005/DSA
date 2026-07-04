class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self,value):
        self.stack.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(self.stack[-1],value))
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        return self.stack[-1]
    def getmin(self):
        return self.minStack[-1]

