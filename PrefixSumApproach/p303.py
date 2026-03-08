class solution(object):
    def __init__(self,nums):
        self.prefix=[0]*len[nums]
        self.prefix[0]=nums[0]
        for i in range (1,len(nums)):
            self.prefix[i]=self.prefix[i-1]+nums[i]
    def sumRange(self,l,r):
        if l==0:
            return self.prefix[r]
        return self.prefix[r]-self.prefix[l-1]
    
