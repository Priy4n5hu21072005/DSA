class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LengthOfTheLinkedList:
    def CountFunction(self,head):
        count = 0 
        current = head
        while current is not None:
            count +=1
            current = current.next 
        return count

object = LengthOfTheLinkedList()
head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
print(object.CountFunction(head))