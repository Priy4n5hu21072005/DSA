
import heapq
class Solution:
    def TopKElement(self,nums:list[int],k:int)->list[int]:
        freq ={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        heap =[]
        for f,num in freq.items():
            heapq.heappush(heap,(f,num))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappush(heap)[1])
        return ans 
