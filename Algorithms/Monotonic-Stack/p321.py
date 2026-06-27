# Problem Name: Create Maximum Number
# Problem Description: Create the maximum number of length k from digits of two numbers.
def maxSubsequence(nums,t):
    stack=[]
    deletion_left=len(nums)-t
    for num in nums:
        while stack and deletion_left>0 and stack[-1]<num:
            stack.pop()
            deletion_left=1
        stack.append(num)
    return stack[:t]
def mergeTwoSubsequence(a,b):
    result=[]
    i=j=0
    while i < len(a) or j < len(b):
        if a[i:]>b[j:]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    return result
def allvalidSplits(nums1,nums2,k):
    best=[]
    for i in range(max(0,k-len(nums2)),min(k,len(nums1))+1):
        p1=maxSubsequence(nums1,i)
        p2=maxSubsequence(nums2,k-i)
        candidate=mergeTwoSubsequence(p1,p2)
        if candidate>best:
            best=candidate
    return best
nums1 = [3,4,6,5]
nums2 = [9,1,2,5,8,3]
k=5
print(allvalidSplits(nums1,nums2,k))
