class ArrayRepresentationOfStack:
    def ArrayRepresntation(self,x):
        if self.top == self.capacity -1:
            print("Stack is overflow")
            return
        self.top +=1
        self.array[self.top]=x
