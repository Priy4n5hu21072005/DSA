# Problem 164 : Maximum Gap Throught the help of Bucket Sort
class Solution(object):
    def MaxGap(self,nums):
        n = len(nums)
        if n <2:
            return 0
        mn=min(nums)
        mx=max(nums)
        if mn==mx:
            return 0
        bs=max(1,(mx-mn+n-2)//(n-1))
        bc=(mx-mn)//bs+1
        b=[[None,None]for _ in range(bc)]
        for num in nums:
            idx=(num-mn)//bs
            if b[idx][0] is None:
                b[idx][0]=num
                b[idx][1]=num
            else:
                b[idx][0]=min(b[idx][0],num)
                b[idx][1]=max(b[idx][1],num)
        mg=0
        pm=b[0][1]
        for i in range(1,bc):
            if b[i][0] is None:
                continue
            mg=max(mg,b[i][0]-pm)
            pm=b[i][1]
        return mg
    
nums=[3,6,1,9]
print(Solution().MaxGap(nums))