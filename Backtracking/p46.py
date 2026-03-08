# this is the problem 46 of permutation 
def permutation(nums):
    n=len(nums)
    if n <= 1:
        return nums
    r=[]
    def back(s):
        if s ==n:
            r.append(nums[:])
            return
        for i in range(s,n):
            nums[s],nums[i]=nums[i],nums[s]
            back(s+1)
            nums[s],nums[i]=nums[i],nums[s]
    back(0)
    return r
nums=[1,2,3]
print(permutation(nums))