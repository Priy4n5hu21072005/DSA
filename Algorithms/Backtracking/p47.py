# Problem Name: Permutations II
# Problem Description: Given a collection of numbers that might contain duplicates, return all possible unique permutations.
def permutationII(nums):
    nums.sort()
    r=[]
    def back(s):
        if s==len(nums):
            r.append(nums[:])
            return
        seen=set()
        for i in range (s,len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[s],nums[i]=nums[i],nums[s]
            back(s+1)
            nums[s],nums[i]=nums[i],nums[s]
    back(0)
    return r
nums=[1,1,2]
print(permutationII(nums))
