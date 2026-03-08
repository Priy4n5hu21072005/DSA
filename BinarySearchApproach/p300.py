def longestIncreaseSubsequence(nums):
    tail=[]
    for n in nums:
        l=0
        r=len(tail)-1
        p=len(tail)
        while l <= r:
            m=(l+r)//2
            if tail[m]>=n:
                p=m
                r=m-1
            else:
                l=m+1
        if p==len(tail):
            tail.append(n)
        else:
            tail[p]=n
    return len(tail)
nums=[10,9,2,5,3,7,101,18]
print(longestIncreaseSubsequence(nums))