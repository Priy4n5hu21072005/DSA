from collections import Counter
import heapq
class Solution:
    def sort_the_string(self,s:str)->str:

        count = Counter(s)

        heap = []

        for char , freq in count.items():

            heapq.heappush(heap,(-freq,char))

        ans = []

        while heap:

            freq,char = heapq.heappop(heap)
            ans.append(char*(-freq))

        return ans 