class Solution:
    def ContigousArray(self,nums:list[int])->int:
        ans = 0
        prefix = 0
        mp = {0:-1}

        for i in range(len(nums)):
            if nums[i]==0:
                prefix-=1
            else:
                prefix+=1

            if prefix in mp:
                distance = i-mp[prefix]
                ans = max(ans,distance)

            else:
                mp[prefix]=i
        return ans 
