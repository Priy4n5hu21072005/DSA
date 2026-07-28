class BruteForceSolution:
    def LLCycleII(self,head:Optional[ListNode])->Optional[ListNode]:
        visited = set()
        current = head
        while current:
            if current in visited:
                return current
            visited.add(current)
            current=current.next  
        return None

class OptimalSolution:
    def DetectCycle(self,head:Optional[ListNode])->Optinal[ListNode]:
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next  
            fast=fast.next.next  

            if slow == fast :
                ptr1 = head
                ptr2=slow

                while ptr1!=ptr2:
                    ptr1=ptr1.next  
                    ptr2=ptr2.next  
                return ptr1
        return None
    