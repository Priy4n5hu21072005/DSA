def selection_sort(self,nums):
    n=len(nums)
    for i in range(n-1):      # time complexity O(n)
        minimum_index=i 

        for j in range(i+1,n):   # time complexity O(n)
            if nums[j]<nums[minimum_index]:
                minimum_index=j
                nums[i],nums[minimum_index]=nums[minimum_index],nums[i]
    return nums  

'''
nums = 1,7,0,5,2
first for loop (4)
        i =0
        min_index=0
        for j(1,5):
            j=1
            nums[j]=7,nums[min_index]=1              7<1   
            if fail
            j=2
            nums[2]=0,nums[min_indx]=1                0<1
            if pass
                min_index=2
                nums=[0,7,1,5,2]
            j=3
            nums[3]=5,nums[min]=1                    5<1
            if fail
            j=4
            nums[4]=2,nums[min]=1                  2<1
            if fail
            
        i=1
        min_indx=1
        for loop(2,4):
            nums[2]=1  nums[min_index]= 7      1<7
            if pass
                nums[0,1,7,5,2]
            j=3
            nums[3]=5,nums[min]=1             5<1
            if fail
            j=4
            nums[4]=2,nums[min]=1             2<1
            if fail
        i=2
        min_index=2
        for loop(3,4):
            nums[3]=5 nums[min]=7            5<7
            if pass
                nums=[0,1,5,7,2]
            j=4
            nums[4]=2 nums[min]=7            2<7
            if pass
                nums=[0,1,5,2,7]

        i=3
        min=3
        for loop(4,5):
            nums[4]=7 nums[3]=2              7<2
            if fail 
        

'''