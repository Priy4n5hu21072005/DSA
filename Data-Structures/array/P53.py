# Problem 53 Maximum SubArray
class Solution:
    def MaxSubarray(self,nums):
        maxSum = nums[0]
        for i in range(len(nums)):
            currSum = 0 
            for j in range(i,len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum,currSum)
        return maxSum
object = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(object.MaxSubarray(nums))