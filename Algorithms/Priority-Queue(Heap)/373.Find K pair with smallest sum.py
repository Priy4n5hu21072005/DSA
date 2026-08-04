import heapq
class Solution:
    def smallestPairs(self,nums1:list[int],nums2:list[int],k:int)->list[list[int]]:
        if not nums1 or not nums2:
            return []
        heap = []
        for i in range(min(len(nums1),k)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))

        ans =[]

        while heap and len(ans)<k:
            total,i,j=heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))

        return ans 
