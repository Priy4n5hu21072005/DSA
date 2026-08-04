class Solution:
    def Find_missing_numbers(self,nums:list[int])->list[int]:
        mn = min(nums)
        mx = max(nums)
        s=set(nums)
        ans = []
        for x in range(mn+1,mx):
            if x not in s:
                ans.append(x)
        return ans 

nums =[5,10,100]
object = Solution()
print(object.Find_missing_numbers(nums))