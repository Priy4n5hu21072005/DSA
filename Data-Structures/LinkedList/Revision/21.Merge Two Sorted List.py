class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def merge_two_sorted_list(self,list1:list[Node],list2:list[Node])->list[Node]:
        dummy = Node(0)
        current=dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next=list1
                list1=list1.next  
            else:
                current.next=list2
                list2=list2.next  
            current=current.next
        if list1:
            current.next=list1
            list1=list1.next   
        else:
            current.next=list2
            list2=list2.next  

        return dummy.next  
    