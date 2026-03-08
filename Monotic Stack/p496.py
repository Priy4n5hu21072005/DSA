# This is the ptoblem of next greater I
def nxtGreater(nums1,nums2):
    stack=[]
    nextGreater={}
    for n in nums2:
        while stack and n > stack[-1]:
            small=stack.pop()
            nextGreater[small]=n
        stack.append(n)
    while stack:
        nextGreater[stack.pop()]=-1
    result=[]
    for n in nums1:
        result.append(nextGreater[n])
    return result
nums1=[4,1,2]
nums2=[1,3,4,2]
print(nxtGreater(nums1,nums2))