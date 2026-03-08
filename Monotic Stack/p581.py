# This is the problem for shortest unsorted continues subarray 
def unsortedSubarray(nums):
    n=len(nums)
    left=n
    stack=[]
    right=0
    for i in range(n):
        while stack and nums[i]<nums[stack[-1]]:
            left=min(left,stack.pop())
        stack.append(i)
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and nums[i]>nums[stack[-1]]:
            right=max(right,stack.pop())
        stack.append(i)
    if right<=left:
        return 0
    return right-left+1
nums=[2,6,4,8,10,9,15]
print(unsortedSubarray(nums))