class BruteForceSolution:
    def maximumCommonSubarray(self,nums1:list[int],nums2:list[int])->int:
        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                length = 0 
                while(i+length<len(nums1) and j+length<len(nums2) and nums1[i+length]==nums2[j+length]):
                    length+=1
                    ans = max(ans,length)
        return ans  