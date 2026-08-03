import heapq
class Solution:
    def Ugly_Number_II(self,n:int)->int:
        visited = {1}
        ugly = 1
        heap = [1]

        for _ in range(n):
            ugly=heapq.heappop(heap)

            for x in (2,3,5):
                new_num = ugly*x
                if new_num not in visited:
                    visited.add(new_num)
                    heapq.heappush(heap,new_num)
        return ugly

n=10 
obj1=Solution()
print(obj1.Ugly_Number_II(n))
