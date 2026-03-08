# This is the problem of arithmatic slice 
def arithmaticSlice(nums):
    n=len(nums)
    if n<3:
        return 0
    count = 0
    current_window=0
    for i in range (2,n):
        if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
            current_window+=1
            count+=current_window
        else:
            current_window=0
    return count
nums = [1,2,3,4]
print(arithmaticSlice(nums))