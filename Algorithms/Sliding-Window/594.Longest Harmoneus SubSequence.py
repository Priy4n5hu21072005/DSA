from collections import Counter
class Solution:
    def LongestHarmoneusSubSequence(self,nums:list[int])->int:
        count = Counter(nums)
        ans = 0
        for n in count:
            if n+1 in count:
                ans = max(ans,count[n]+count[n+1])
        return ans