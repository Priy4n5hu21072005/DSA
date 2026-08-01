class Solution:
    def ContinuesSubarraySum(self,nums:list[int],k:int)-> bool:

        map = {0,-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            reminder = prefix % k

            if reminder in map:

                if i - map[reminder]>=2:
                    return True

                else:
                    map[reminder]=i

        return False
    