import heapq
class Solution:
    def max_profit(self,k:int,w:int,profits:list[int],capital:list[int])->int:
        projects = list(zip(capital,profits))
        projects.sort(key=lambda x :x[0])
        maxHeap=[]
        i,n=0,len(projects)
        for _ in range(k):
            while i<n and projects[i][0]<=w:
                heapq.heappush(maxHeap,-projects[i][1])
                i+=1

            if not maxHeap:
                break

            w+=-heapq.heappop(maxHeap)
        return w

k=2
w=0 
capital=[0,1,1]
profits=[1,2,3]
object=Solution()
print(object.max_profit(k,w,profits,capital))
