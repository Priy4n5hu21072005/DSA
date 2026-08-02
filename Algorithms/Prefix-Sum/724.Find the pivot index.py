class Solution:
    def PivotAlgorithm(self,nums:list[int])->int:
        total_sum=sum(nums)
        left =  0
        for i in range(len(nums)):
            right = total_sum-left-nums[i]
            if left==right:
                return i
            left+=nums[i]

        return -1