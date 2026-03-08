def sortColor(nums):
    n = len(nums)
    left =0
    right=n-1
    i=0
    while i <=right:
        if nums[i]==0:
            nums[i],nums[left]=nums[left],nums[i]
            left +=1
            i +=1
        elif nums[i]==2:
            nums[i],nums[right]=nums[right],nums[i]
            right -=1
        if nums[i]==1:
            i +=1
            

    
