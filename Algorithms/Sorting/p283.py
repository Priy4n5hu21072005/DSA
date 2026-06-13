class Solution:
    def MovesZeroes(self,nums):
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        return nums
object=Solution()
nums=[0,1,0,3,12]
print(object.MovesZeroes(nums))