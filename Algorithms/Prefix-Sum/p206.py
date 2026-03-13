# Problem Name: Minimum Size Subarray Sum
# Problem Description: Return the minimal length of a contiguous subarray of which the sum is greater than or equal to target.
class solution(object):
    def miniSize(self,nums,target):
        left =0
        sum=0
        length=float('inf')
        for right in range (len(nums)):
            sum += nums[right]
            while sum >= target:
                length=min(length,right-left-1)
                sum -= nums[left]
                left +=1
        if length == float('inf'):
                return 0
        return length

