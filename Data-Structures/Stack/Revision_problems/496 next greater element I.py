class Solution:
    def nextGreater(self,nums1:list[int],nums2:list[int]):
        stack=[]
        nextgreater={}
        for i in nums2:
            while stack or stack[-1]<i:
                nextgreater(stack.pop())=i
            stack.append(i)   

        ans=[]
        for i in nums1:
            ans.append(nextgreater.get(i,-1))
        return ans
