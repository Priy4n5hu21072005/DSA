class Solution:
    def smallest_stable_index_II(self,nums:list[int],k:int)->int:
        suffex_min=[0]*len(nums)
        suffex_min[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffex_min=min(nums[i],suffex_min[i+1])
        left_max=float('-inf')
        for i in range(len(nums)):
            left_max=max(left_max,nums[i])
            ins =left_max-suffex_min[i]
            if ins<=k:
                return i
        return -1


'''
nums=[5,0,1,4],k=3
suffex=[0,0,0,0]
suffex=[0,0,0,4]
for i in range(2,-1,-1):
    i=2
    suffex_min[2]=min(nums[2],suffex[2+1])
                  min(1,4)
    suffex=[0,0,1,4]
    i=1
    suffex[1]=min(nums[1],suffex[1+1])
                min(0,1)
    suffex=[0,0,1,4]
    i=0
    suffex[0]=min(nums[0],suffex[0+1])
                min(5,0)
    suffex=[0,0,1,4]
left_max=-inf
for i in range(4):
    i=0
    left_max=max(left_max,nums[0])
            max(-inf,5)
    left_max=5
    ins=left_max-suffex[0]
      ins=5-0=5
      if 5<=3 fail
    i=1
    left_max=max(5,0)
    ins=5-0=5
    if fail
    
    i=2
    left_max=max(5,1)
    ins=5-1=4
    if fail
    
    i=3
    left_max=max(5,4)
    ins=5-4=1
    if pass
    return 3
    '''