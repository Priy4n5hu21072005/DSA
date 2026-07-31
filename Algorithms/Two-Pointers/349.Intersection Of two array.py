class Solution :
    def UniqueElement(self,nums1:list[int],nums2:list[int])->list[int]:
        return list(set(nums1)&set(nums2))

nums1=[1,2,2,3]
nums2=[2,2]
object = Solution()
print(object.UniqueElement(nums1,nums2)) 