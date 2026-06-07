class Solution:
    def TwoSum(self,nums,target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
obj=Solution()
nums=[2,7,3,3]
target=9
print(obj.TwoSum(nums,target))

# Time Complexity is O(n^2)
# Space Complexity is O(1)
# Optimal Solution
class Solution2:
    def TwoSum(self,nums,target):
        hp={}
        for i ,num in enumerate(nums):
            req=target-num
            if req in hp:
                return [hp[req],i]
            hp[num]=i
obj=Solution2()
nums=[2,7,3,3]
target=9
print(obj.TwoSum(nums,target))

class Solution3:
    def TwoSum(self,nums,target):
        nums.sort()
        left =0
        right = len(nums)-1
        while left < right:
            mid = nums[left]+nums[right]
            if mid == target:
                return [left,right]
            elif mid < target:
                left +=1
            else :
                right -=1