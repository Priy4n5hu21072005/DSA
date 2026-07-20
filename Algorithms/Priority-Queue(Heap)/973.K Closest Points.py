import heapq
class Solution:
    def KClosestPoints(self,points : list[str],k:int)-> list[list[int]]:
        heap =[]
        for x,y in points:
            dis = x*x +y*y 
            heapq.heappush(heap,(-dis,x,y))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        while heap:
            dis,x,y=heapq.heappop(heap)
            ans.append([x,y])
        return ans 

points = [[1,3],[-2,2]]
k=1 
object=Solution()
print(object.KClosestPoints(points,k))