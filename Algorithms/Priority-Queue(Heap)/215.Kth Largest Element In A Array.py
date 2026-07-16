import heapq
class BruteSolution:
    def KthLargestElement(self,nums:list[int],k:int)->int:
        nums.sort()
        return nums[-k]
    
class DimagWalaSolution:
    def KthLargestElement(self,nums:list[int],k:int)->int:
        heap =[]
        for x in nums:
            heapq.heappush(heap,x)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
obj1=DimagWalaSolution()

obj = BruteSolution()
nums = [3,2,1,5,6,4]
k=3  
print(obj.KthLargestElement(nums,k))
print(obj1.KthLargestElement(nums,k))
