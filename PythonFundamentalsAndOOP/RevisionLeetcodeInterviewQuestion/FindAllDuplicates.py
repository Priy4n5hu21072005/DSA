class BachoWalaSolution:
    def AllDuplicates(self,nums):
        if not nums :
            return 0
        hm =[]
        for i in range (len (nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count +=1
            if count > 1 and nums[i] not in hm:
                hm.append(nums[i])
        return hm
nums = [1,3,2,3]
obj = BachoWalaSolution()
print(obj.AllDuplicates(nums))

class HackerWalaSolution:
    def AllDuplicates(self,nums):
        freq ={}
        ans = []
        for cn in nums:
            freq[cn]=freq.get(cn,0)+1
        for idx,value in freq.items():
            if value ==2:
                ans.append(idx)
        return ans
nums = [1,3,2,3]
obj = HackerWalaSolution()
print(obj.AllDuplicates(nums))