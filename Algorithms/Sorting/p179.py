# Problem 179 : Largest Number
# Input : nums =[3,30]
# Output : "330"
from functools import cmp_to_key
# Basically cmp_to_key is a function that converts a comparison function into a key function.
# for example, if you have a comparison function that compares two elements and returns -1, 0, or 1, you can use cmp_to_key to create a key function that can be used with sorting functions like sorted() or list.sort().
class Solution(object):
    def LargestNumber(self,nums):
        nums=list(map(str,nums))
        def compare(a,b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            return 0
        nums.sort(key=cmp_to_key(compare))
        result="".join(nums)
        return '0' if result[0]=='0' else result
nums=[3,30]
print(Solution().LargestNumber(nums))
        