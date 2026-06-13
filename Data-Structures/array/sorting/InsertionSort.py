def InsertionSort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1 
        while j >= 0 and key < nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
if __name__=="__main__":
    nums = [12,11,13,5,6]
    InsertionSort(nums)
    for i in range(len(nums)):
        print(nums[i],end=" ")
