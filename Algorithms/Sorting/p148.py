# Problem 148: Sort List
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution(object):
    def SortList(self,head):
        if not head or not head.next:
            return head
        s=head
        f=head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        mid=s.next 
        s.next=None

        l=self.SortList(head)
        r=self.SortList(mid)
        return self.merge(l,r)


    def merge(self,l,r):
        dummy=ListNode(0)
        curr=dummy
        while l and r:
            if l.val<=r.val:
                curr.next=l
                l=l.next
            else:
                curr.next=r
                r=r.next
            curr=curr.next
        if l:
            curr.next=l
        else:
            curr.next=r
        return dummy.next