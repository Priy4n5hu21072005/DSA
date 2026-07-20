from collections import Counter
import heapq
class Solution:
    def TopKFrequentElement(self,words:list[str],k:int)-> list[str]:
        heap =[]
        freq = Counter(words)
        for w,count in freq.items():
            heapq.heappush(heap,(-count,w))
        ans = []
        for _ in range(k):
            count,w = heapq.heappop(heap)
            ans.append(w)
        return ans  
    
words = ["i","love","you","i","love"]
k = 3
object =Solution()
print(object.TopKFrequentElement(words,k))