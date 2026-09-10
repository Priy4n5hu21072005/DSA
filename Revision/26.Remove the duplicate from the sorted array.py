def remove_duplicate_the_sorted_array(nums):
    i=0 
    for j in range(len(nums)):
        if nums[i]!=nums[j]:
            i+=1
        nums[i]=nums[j]
    return i+1


'''
nums=[1,2,2,3,1]
j loop = 5
j=0
if nums[0]!=nums[0]  1=1 fail
nums[0]=nums[0]=nums[1,2,2,3,1]

j=1
if nums[0]!=nums[1]  1!=2 pass
    i=1
nums[1]=nums[1]  nums=[1,2,2,3,1]

j=2
if nums[1]!=nums[2]  2!=2 fail
nums[1]=nums[2]   nums=[1,2,3,1,_]

j=3
if nums[1]!=nums[3]    2!=3 pass
    i=2
nums[2]=nums[3]   nums[1,2,3,1,_]

j=4
if nums[2]!=nums[4]'''
        
