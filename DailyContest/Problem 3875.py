class Solution:
    def create_nums2(self,nums1:list[int])->bool:
        #ek minmum odd number ko maintain karana
        min_odd=float('inf')
        for i in nums1:
            if i % 2 != 0:
                min_odd=min(min_odd,i)
        #agar koi odd number nahi mila tab
        if min_odd == float('inf'):
            return True
        #minimum even number ko dekhna ki vo odd se chota hai ki nahi 
        for x in nums1:
            if x % 2 == 0 and min_odd>x:
                return False
        return True


