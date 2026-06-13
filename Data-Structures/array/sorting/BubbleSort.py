def BubbleSort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(0,len(nums)-i-1):
            if nums[j]> nums[j+1]:
                nums[j+1],nums[j]=nums[j],nums[j+1]
                swapped = True
        if (swapped == False):
            break
    return nums
if __name__ == "__main__":
    nums =[5,6,1,3]
    BubbleSort(nums)
    for i in range(len(nums)):
        print(nums[i],end=" ")