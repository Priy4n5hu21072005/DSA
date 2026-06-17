class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class SearchInLinkedList:
    def SearchFunction(self,head,key):
        current = head 
        while current is not None:
            if current.data == key :
                return True
            current = current.next  
        return False

object = SearchInLinkedList()
head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
key = 2
print(object.SearchFunction(head,key))