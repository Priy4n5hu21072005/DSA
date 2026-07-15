import heapq
class Solution:
    def Problem1046(self,nums):
        mh=[-x for x in nums]
        heapq.heapify(mh)

        while len(mh)>1:
            first = -heapq.heappop(mh)
            second = -heapq.heappop(mh)
            dif = first-second
            if dif >0:
                heapq.heappush(mh,-dif)
        return -mh[0] if mh else 0

stones = [2,7,4,1,8,1]
obj = Solution()
print(obj.Problem1046(stones)) 