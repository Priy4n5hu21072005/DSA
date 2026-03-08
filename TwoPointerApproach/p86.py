# This is the partition list problem
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.next=next
class partitionNode(object):
    def partition(head,x):
        smallDummy=ListNode(0)
        largeDummy=ListNode(0)
        small=smallDummy
        large=largeDummy
        current=head
        while current:
            if current.val<x:
                small.next=current
                small=small.next
            else :
                large.next=current
                large=large.next
            current=current.next
        large.next=None
        small.next=largeDummy.next
        return smallDummy.next
