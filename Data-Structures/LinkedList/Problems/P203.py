class ListNode:
    def __init__(self,data,val = 0):
        self.data = data 
        self.val = val 
        self.next = None
class Solution:
    def RemoveLLElement(self,head,val):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy 
        curr = head 
        while curr :
            if curr.val == val :
                prev.next = curr.next  
            else:
                prev = curr  
            curr = curr.next  
        return dummy.next  