'''
dekh isme 2 cheeze di hai target and n humein bas ye batana hai ki stream ka element target ke element 
ke equal hai toh push nahi hai toh pahle push then pop 
for example target =[1,3] and n =3
toh stream banegi = 1,2,3
theek hai ab 1==1 hai toh push khali 
ab 2 nahi chayie taregte mein toh pahle push then pop 
toh output hoga ["push","push","pop","push"]
'''
class Solution:
    def BuildArray(self,target,n):
        ans = []
        current = 1
        for i in target:
            while current < i :
                ans.append("push")
                ans.append("pop")
                current+=1
            ans.append("push")
            current+=1
        return ans