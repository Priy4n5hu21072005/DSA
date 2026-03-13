# Problem Name: Product of Array Except Self
# Problem Description: Return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
class solution(object):
    def productExceptItself(nums):
        n = len(nums)
        ans=[1]*n
        left_side=1
        for i in range (n):
            ans[i]=left_side
            left_side*=nums[i]
        right_side=1
        for i in range (n-1,-1,-1):
            ans[i]*=right_side
            right_side*=nums[i]
        return ans
