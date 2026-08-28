class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverse_linked_list(self,head:list[Node])->list[Node]:
        prev=None
        current=head
        while current:
            next_node=current.next  
            current.next=prev
            prev=current
            current=next_node
        return prev


'''
[13,14,10,9]
o/p->[9,10,13,14]
prev=None
current=13
while pass
    next=14
    13->None(prev)
    prev=13
    current=14

while pass current =14
    next=10
    14->13(prev)->None
    prev=14
    current=10

while current=10 pass
    next=9
    10->14->13->None
    prev=10
    current=9

while current = 9 pass 
    next=None
    9->10->14->13
    prev=9
    current=None
while fail

return prev = 9>10


'''