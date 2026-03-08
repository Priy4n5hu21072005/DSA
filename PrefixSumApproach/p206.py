# Minimum size of sub Array
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

