class Solution:
    def Equilibrium(self,nums:list[int])->int:
        total=sum(nums)
        index=0  
        left=0
        for index in range(len(nums)):
            right= total-left-nums[index]
            if left==right:
                return index
            left+=nums[index]
        return -1

nums=[1,2,0,3]
object=Solution()
print(object.Equilibrium(nums))
