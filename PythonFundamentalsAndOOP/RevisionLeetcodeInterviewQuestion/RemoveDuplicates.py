class Solution:
    def Duplicates(self,nums):
        if not nums:
            return 0
        unique = sorted(set(nums))
        for i in range (len(unique)):
            nums[i]=unique[i]
        return len(unique)

class Solution2:
    def Duplicates(self, nums):
        if not nums:
            return 0
        i =0
        for j in range (len(nums)):
            if nums[j]!=nums[i]:
                i+=1
            nums[i]=nums[j]
        return i+1
