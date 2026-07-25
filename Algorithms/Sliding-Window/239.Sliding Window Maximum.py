from collections import deque
class Solution :
    def SlidingWindowMaximum(self,nums:list[int],k:int)->list[int]:
        qu = deque
        ans = []

        for i in range(len(nums)):

            while qu and qu[0]<=i-k:
                qu.popleft()

            while qu and nums[qu[-1]]<nums[i]:
                qu.pop()

            qu.append(i)

            if i>=k-1:
                ans.append(nums[qu[0]])

        return ans   