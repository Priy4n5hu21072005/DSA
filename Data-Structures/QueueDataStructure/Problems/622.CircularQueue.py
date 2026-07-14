from collections import deque
class sol:
    def __init__(self,k):
        self.qu = [0]*k
        self.front = 0
        self.rear = -1
        self.capacity = k
        self.size=0  
    def enQueue(self,val):
        if self.capacity == self.size:
            return False
        if self.rear == self.capacity-1:
            self.rear=0
        else:
            self.rear +=1
        self.qu[self.rear]=val
        self.size +=1
        return True
    def deQueue(self):
        if self.size==0:
            return False
        if self.front==self.capacity-1:
            self.front = 0
        else:
            self.front +=1
        self.size-=1
        return True
    def Front(self):
        return self.qu[self.front]
    def Rear(self):
        return self.qu[self.rear]
    def isEmpty(self):
        if self.size==0:
            return True
        return False
    def isFull(self):
        if self.capacity==self.size:
            return True
        return False


