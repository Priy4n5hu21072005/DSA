# Problem Name: Contains Duplicate III
# Problem Description: Find a pair of indices (i, j) such that |i - j| <= indexDiff and |nums[i] - nums[j]| <= valueDiff.
'''
input = [1,2,3,4,1]
indexdiff=4
valuediff=0
return True 
'''

def containDuplicateII(nums,indexdiff,valuediff):
    n=len(nums)
    window=[]
    for i in range (n):
        for val in window:
            if abs (nums[i]-val)<=valuediff:
                return True
        window.append(nums[i])

        if len(window)> indexdiff:
            window.pop(0)
    return False

    '''
    for i in range (n):
        for j in range (n):
            if i !=j:
                if abs(i-j)<=indexdiff and abs(nums[i]-nums[j])<=valuediff:
                    return True
    return False
    '''
input = [1,2,3,4,1]
indexdiff=4
valuediff=0
print(containDuplicateII(input,indexdiff,valuediff))

