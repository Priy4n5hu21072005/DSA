# Problem 3737 : Problem simple hai humein ek array given hai and ek target given hai ab humein aise subarray nikalana hai jiski majar length
# jyada ho for example array = [1,2,2,3,3] and target = 2
# subarray where target length kuch aisa [1,2],[1,2,2],[1,2,2,3],[1,2,2,3,3],[2,2],[2,2,3],[2,2,3,3],[2,3],[2,3,3]

class Solution:
    def MajorSubarray(self,nums,target):
        ans = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    count += 1
                length = j-i+1
                if count > length//2:
                    ans +=1
        return ans
nums = [1,2,2,3]
target =2
object = Solution()
print(object.MajorSubarray(nums,target))