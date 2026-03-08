# this is the problem 456 of 132 pattern 
def findPattern(nums):
    if not nums:
        return False
    stack=[]
    second=float('-inf')
    for right in range(len(nums)-1,-1,-1):
        if nums[right]<second:
            return True
        while stack and stack[-1]<nums[right]:
            second=stack.pop()
        stack.append(nums[right])
    return False
nums=[3,1,4,2]
print(findPattern(nums))
            