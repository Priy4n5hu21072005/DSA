# Problem Name: Search in Rotated Sorted Array II
# Problem Description: Return true if target is in the rotated sorted array, or false if it is not.
def searchArray(nums,target):
    low =0
    high=len(nums)-1
    while low <= high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
        elif nums[low]<=nums[mid]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]< target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False
nums = [2,5,6,0,0,1,2] 
target = 0
print(searchArray(nums,target))

    