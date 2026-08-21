def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        prev=i-1   
        while prev >= 0 and key<nums[prev]:
            nums[prev+1]=nums[prev]
            prev-=1   # prev = prev - 1
        nums[prev+1]=key


nums=12,11,13,5,6
'''
for (1,5):
    i=1
    key=11
    prev=i-1    = 0

    while 0>=0 pass and  11<nums[0]   11<12 pass:
        nums[1]=nums[0]  = nums[1]=12                 nums[0+1]=nums[1]=nums[0]=12 ,nums[1]=12
        nums=[11,12,13,5,6]
        prev = 0-1=-1
    nums[0]=11=key # nums[prev+1]=key nums[-1+1]=key  nums[0]=key 11=key
                  #  -1+1=0

    key =11
    prev=-1

    while fail
    
    i=2
    key=nums[2]=13
    prev=i-1=1
    while pass and 13<nums[1]  13<12 fail
                prev=0
    while pass and 13<nums[0] 13<11 fail
    nums=[11,12,13,5,6]
    i=3
    key=nums[i]=5
    prev=i-1=2
    while pass and 5<nums[prev]  5<13 pass
        nums[2]=5
        prev=1
    while pass 5<12 pas
        nums[1]=5
        prev=0
    while 0>=0 pass 5<11 pass
        nums[0]=5
        

    
    

'''