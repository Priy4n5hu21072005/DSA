from collections import Counter
class Solution:
    def MaxLength(self,nums):
        freq = Counter(nums)
        ans = 1
        if 1 in freq:
            ans = freq[1] if freq[1]%2 else freq[1]-1
        for x in freq:
            if x == 1:
                continue
            current = x
            deapth = 0
            while freq.get(current,0)>= 2:
                deapth +=1
                current=current*current
            if freq.get(current,0)>=1:
                ans = max(ans,2*deapth+1)
            else:
                ans = max(ans,2*deapth-1)
        return ans