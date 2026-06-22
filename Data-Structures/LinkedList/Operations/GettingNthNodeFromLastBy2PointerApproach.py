class Node:
    def __init__(self,data):
        self.data = data  
        self.next = None
class GettingNthNodeFromLastBy2Pointer:
    def GettingFunction(self,head,k):
        main_pointer = head 
        ref_pointer = head 
        for _ in range (1,k):
            ref_pointer = ref_pointer.next  
            if ref_pointer is None:
                return -1
        while ref_pointer.next is not None:
            main_pointer=main_pointer.next  
            ref_pointer=ref_pointer.next  
        return main_pointer.data  