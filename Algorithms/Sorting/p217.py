# Problem 217 : Contains Duplicate
# input nums :[1,2,3,1]
# output : true
class Solution(object):
    def ContainsDuplicate(self,nums):
        return len(nums)!=len(set(nums))
nums = [1,2,3,1]
print(Solution().ContainsDuplicate(nums))