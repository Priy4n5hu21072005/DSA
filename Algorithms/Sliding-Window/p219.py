# Problem Name: Contains Duplicate II
# Problem Description: Return true if there are two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
class solution(object):
    def containDuplicates(self,nums,k):
        window=set()
        left =0
        for right in range (len(nums)):
            if nums[right] in window:
                return True
            window.add(nums[right])
            if right-left >=k:
                window.remove(nums[left])
                left +=1
        return False
nums =[1,0,1,1]
k=3
obj=solution()
print(obj.containDuplicates(nums,k))