class Solution:
    def SelectionSort(self,nums):
        n = len(nums)
        for i in range(n-1):
            min_idx = i   
            for j in range (i+1,n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i],nums[min_idx] = nums[min_idx],nums[i]
        return nums

Obj = Solution()
nums=[64,25,12,22,11]
print(Obj.SelectionSort(nums))