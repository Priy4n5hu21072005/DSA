class sol:
    def __init__(self):
        self.inputstack =[]
        self.outputstack=[]
    def push(self,x):
        self.inputstack.append(x)
    def pop(self):
        if not self.outputstack:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack.pop()
    def peek(self):
        if not self.outputstack:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack[-1]
    def empty(self):
        return len(self.inputstack)==0 and len(self.outputstack)==0
