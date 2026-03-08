def combinationsumII(nums,target):
    nums.sort()
    r=[]
    def back(s,rem,c):
        if rem==0:
            r.append(c[:])
            return
        for i in range(s,len(nums)):
            if i >s and nums[i]==nums[i-1]:
                continue
            if nums[i]>rem:
                break
            c.append(nums[i])
            back(i+1,rem-nums[i],c)
            c.pop()
    back(0,target,[])
    return r
nums=[10,1,2,7,6,1,5]
target=8
print(combinationsumII(nums,target))
        