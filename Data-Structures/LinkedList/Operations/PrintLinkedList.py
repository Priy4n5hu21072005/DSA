class Node:
    def __init__(self,data):
        self.data = data  
        self.next = None
class PrintLinkedList:
    def PrintFunction(self,node):
        while node is not None:
            print(f"{node.data}",end="")
            if node.next is not None:
                print("->",end="")
            node = node.next  
        print()
object = PrintLinkedList()
head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
result =object.PrintFunction(head)
print(result)