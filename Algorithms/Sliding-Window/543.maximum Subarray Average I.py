class Solution:
    def MaximumAverageSubarrayI(self,nums:list[int],k:int):
        window = 0 
        for i in range(k):
            window += nums[i]
        max_sum = window
        for i in range(k,len(nums)):
            window += nums[i]
            window -= nums[i-k]
            if window > max_sum:
                max_sum=window
        return max_sum/k