class BachoWalaSolution:
    def Major(self,nums):
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                if count > len(nums)//2:
                    return nums[i]

class HackerWalaSolution:
    def Major(self,nums):
        freq ={}
        for cn in nums:
            freq[cn]=freq.get(cn,0)+1
        for key,value in freq.items():
            if value > len(nums)//2:
                return key