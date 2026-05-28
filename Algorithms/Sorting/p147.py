# Problem 147 : Insertion sort List
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next

class Solution(object):
    def SortList(self,head):
        dummy =ListNode(0)
        curr=head
        while curr:
            prev=dummy
            # Position find
            while prev.next and prev.next.val < curr.val:
                prev=prev.next
            nxt=curr.next
            # Insertion Sorting
            curr.next = prev.next
            prev.next=curr
            curr=nxt
        return dummy.next
    
