class Solution:
    def Problem1927(self,num:str)->bool:
        left_q=0
        right_q=0
        left_sum=0
        right_sum=0
        for i in range(len(num)//2):
            if num[i]=="?":
                left_q+=1
            else:
                left_sum+=int(num[i])
        for i in range(len(num)//2,len(num)):
            if num[i]=="?":
                right_q+=1
            else:
                right_sum+=int(num[i])
        if left_q != right_q:
            return True

        return abs(left_sum-right_sum) != 9*left_q
