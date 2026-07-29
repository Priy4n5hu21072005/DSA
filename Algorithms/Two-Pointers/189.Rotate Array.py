class Solution:
    def RotateArray(self,nums:list[int],k:int)->list[int]:
        if k == 0 :
            return nums
        k%=len(nums)
        ans=[]
        for i in range(len(nums)-k,len(nums)):
            ans.append(nums[i])
        for i in range(0,len(nums)):
            ans.append(nums[i])
        return ans 

nums=[1,2,3,4,5,6,7]
k=3 
obj1=Solution()
print(obj1.RotateArray(nums,k))


