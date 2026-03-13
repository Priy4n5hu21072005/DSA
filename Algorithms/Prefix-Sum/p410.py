# Problem Name: Split Array Largest Sum
# Problem Description: Split the array into m non-empty continuous subarrays to minimize the largest sum.
class solution(object):
    def splitArray(self,nums,k):
        def canSplit(maxSum):
            sub_arrays=1
            current=0
            for num in nums:
                if current + num > maxSum:
                    sub_arrays +=1
                    current=num
                else :
                    current +=num
            return sub_arrays<=k
        low = max(nums)
        high=sum(nums)
        while low < high :
            mid = (low+high)//2
            if canSplit(mid):
                high=mid
            else:
                low =mid+1
        return low
nums=[7,2,3,10,8]
k=2
obj=solution()
print(obj.splitArray(nums,k))