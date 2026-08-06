from collections import defaultdict
import heapq
class Solution:
    def SplitArray(self,nums:list[int])->bool:
        heaps=defaultdict(list)
        for num in nums:
            if heaps[num-1]:
                small_lenght = heapq.heappop(heaps[num-1])
                heapq.heappush(heaps[num],small_lenght+1)

            else:
                heapq.heappush(heaps[num],1)

        for heap in heaps.values():
            while heap:
                if heapq.heappop(heap)<3:
                    return False
        return True

nums=[1,2,3,3,4,5]
nums1=[1,2,3,4,4,5]
object=Solution()
print(object.SplitArray(nums))
print(object.SplitArray(nums1))


