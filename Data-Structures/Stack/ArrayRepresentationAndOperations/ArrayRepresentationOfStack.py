# Insert Operation
# Time complexity is O(1)
class ArrayRepresentationOfStack:
    def ArrayRepresntation(self,x):
        if self.top == self.capacity -1:
            print("Stack is overflow")
            return
        self.top +=1
        self.array[self.top]=x

    # Pop Operation
    # time complexity = O(1)
    def pop(self):
        if self.top==-1:
            print("Stack is underflow")
            return -1
        values = self.arr[self.top]
        self.top -=1
        return values