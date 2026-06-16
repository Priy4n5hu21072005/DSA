class Solution:
    def MaxSubArray(self,nums):
        maxSum = nums[0]
        currSum = 0
        for i in nums:
            currSum += i
            maxSum = max(maxSum,currSum)
            if currSum < 0 :
                currSum = 0
        return maxSum  
