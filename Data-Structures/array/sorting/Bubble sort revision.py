'''
dekh jaise ek array hai 
5,6,1,3 
ab initially bubble
5,6,1,3
|              5>6 swap nahi toh bubble aage shift
5,6,1,3
  |            6>1 swap (value)
5,1,6,3
    |          6>3 swap(value)

5,1,3,6
      |        now bubble wapas se 0th index pe chala gaya


'''
def bubble_sort(nums):
    for i in range(len(nums)):       # time complexity - O(n)
        swapped = False
        for j in range(0,len(nums)-i-1):     # time complexity - O(n)
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
        if (swapped==False):
            break