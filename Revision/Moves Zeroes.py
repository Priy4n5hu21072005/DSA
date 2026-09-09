def moves_zeroes(nums):
    i=0  
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1

'''
[0,1,0,2,3]
o/p=[1,2,3,0,0]
for j loop 5
j=0
if fail
nums[0]=0!=0 fail
j=1
nums[1]=1!=0 true
nums=[1,0,0,2,3]
i=1
j=2
nums[2]=0!=0
j=3
nums[3]=2!=0 true
nums=[1,2,0,0,3]
i=2
j=4
nums[4]=3!=0
nums=[1,2,3,0,0]

'''