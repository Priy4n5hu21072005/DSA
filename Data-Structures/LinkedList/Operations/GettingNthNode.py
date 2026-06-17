class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class GetNthNode:
    def GetFunction(self,head,index):
        current = head 
        count = 0
        while current is not None:
            if count == index:
                return current.data  
            count +=1
            current = current.next  
        return -1
head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
key = 2
object = GetNthNode()
print(object.GetFunction(head,key))