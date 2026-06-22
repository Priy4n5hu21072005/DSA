class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class GettingNthNodeFromLast:
    def GettingFunction(self,head,k):
        lenght = 0 
        current = head 
        while current :
            lenght +=1
            current=current.next  
        if lenght < k:
            return -1
        current = head
        for _ in range (1,lenght-k+1):
            current = current.next  
        return current.data  