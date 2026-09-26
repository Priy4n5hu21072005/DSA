#Humein ek unsorted array diya hai aur humein consecutive longest subsequence nikalana hai 

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        if not nums:
            return 0
        
        parent={}
        size={}
        for num in nums:
            parent[num]=num
            size[num]=1

        def find(i):
            if parent[i]==i:
                return i
            parent[i]=find(parent[i])
            return parent[i]

        
        def union(a,b):
            arep=find(a)  
            brep=find(b)  
            if arep != brep:
                parent[brep]=arep
                size[arep]+=size[brep]

        for num in nums:
            if num+1 in nums:
                union(num,num+1)

        return max(size.values())