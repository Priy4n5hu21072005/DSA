class Solution:
    def smallest_stable_index_i(self,nums:list[int],k:int)->int:
        m1=float('-inf')
        for i in range(len(nums)):
            m1=max(m1,nums[i])
            m2=min(nums[i:])
            ins=m1-m2
            if ins<=k:
                return i
        return -1
    
