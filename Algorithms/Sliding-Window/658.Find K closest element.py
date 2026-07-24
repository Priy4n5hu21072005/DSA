class Solution :
    def FindKClosestElement(self,nums:list[int],k:int,x:int)->list[int]:
        l = 0 
        r = len(nums)-1
        while True :
            window_size = r-l+1

            if window_size == k:
                break

            ld=abs(nums[l]-x)
            rd=abs(nums[r]-x)

            if ld>rd:
                l+=1
            else:
                r-=1
        return nums[l:r+1]