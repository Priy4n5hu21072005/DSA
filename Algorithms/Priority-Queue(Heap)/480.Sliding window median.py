from collections import defaultdict
import heapq
class Solution:
    def Sliding_Window_Median(self,k:int,nums:list[int])->list[int]:
        small=[]
        large=[]
        delayed=defaultdict(int)
        small_size=0
        large_size=0

        def prune(heap):
            while heap:
                if heap==small:
                    num=-heap[0]
                else:
                    num=heap[0]
                if delayed[num]:
                    heapq.heappop(heap)
                    delayed[num]-=1
                else:break

        def rebalance():
            nonlocal small_size  , large_size
            if small_size>large_size+1:
                x=-heapq.heappop(small)
                heapq.heappush(large,x)
                small_size-=1
                large_size+=1
                prune(small)
            elif small_size<large_size:
                x=heapq.heappop(large)
                heapq.heappush(small,x)
                small_size+=1
                large_size-=1
                prune(large)

        def add(num):
            nonlocal small_size,large_size
            if not small or num <= -small[0]:
                heapq.heappush(small,-num)
                small_size+=1
            else:
                # comment: 
                heapq.heappush(large,num)
                large_size+=1
            rebalance()

        def remove(num):
            nonlocal small_size,large_size
            delayed[num]+=1
            if num <= -small[0]:
                small_size-=1
                if num==-small[0]:
                    prune(small)
            else:
                large_size-=1
                if large and num==large[0]:
                    prune(large)
            rebalance()

        def get_median():
            if k%2 :
                return float(-small[0])
            return(-small[0]+large[0])/2
        for i in range(k):
            add(nums[i])

        ans=[get_median()]

        for i in range(k,len(nums)):
            add(nums[i])
            remove(nums[i-k])
            ans.append(get_median())
        return ans  
         

