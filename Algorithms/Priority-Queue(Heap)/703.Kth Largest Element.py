import heapq
class Solution:
    def __init__(self,k,nums):
        self.k = k 
        self.heap = []
        for n in nums:
            self.add(n)
    def add(self,val):
        if len(self.heap)<self.k:
            heapq.heapify(self.heap,val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]
    

       
