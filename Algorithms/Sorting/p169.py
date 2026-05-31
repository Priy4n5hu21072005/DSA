# Problem 169 : Majority element
# Input : nums = [2,3,2,1,2]
# Output : 2
class Solution(object):
    def Major(self,nums):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]> len(nums)//2:
                return num

# Optimal Solution
# return max(set(nums),key=nums.count)

nums =[2,3,2,1,2]
print(Solution().Major(nums))
            