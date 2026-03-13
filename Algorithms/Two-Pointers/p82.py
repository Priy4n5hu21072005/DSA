# Problem Name: Remove Duplicates from Sorted List II
# Problem Description: Delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.next=next
        self.val=val
class solution(object):
    def removeDuplicateList(head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr=curr.next
                prev.next=curr.next
            else :
                prev=prev.next
            curr=curr.next
        return dummy.next