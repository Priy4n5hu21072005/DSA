class Solution:
    def findGCD(self,nums:list[int])->int:
       return self.findGCD(max(nums),min(nums))
        