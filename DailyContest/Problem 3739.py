# Dekh Problem 3737 ki tarah same he hai par iska optimize version hai bas jaha constraints thode hard ho jaate hai
from django.db.models.expressions import result
from optree.version import prefix


class Solution:
    def MajoritySubarrayII(self,nums,target):
        count = [0]*((2*len(nums)+1)+1)
        prefix = [0]*((2*len(nums)+1)+1)
        prefix[0]=1
        count[0]=1
        result = 0
        current = 0
        for i in nums :
            current +=1 if i == target else -1
            count[current]+=1
            prefix[current]=prefix[current-1]+count[current]
            result += prefix[current-1]
        return result