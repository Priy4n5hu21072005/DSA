from collections import Counter
class Solution:
    def CommonElement(self,nums1:list[int],nums2:list[int])->list[int]:
        freq = Counter(nums1)
        ans=[]
        for n in nums2:
            if n in freq and freq[n]>0:
                ans.append(n)  
                freq[n]-=1

        return ans 

nums1=[1,2,2,3]
nums2=[2,2,4]
object = Solution()
print(object.CommonElement(nums1,nums2))
