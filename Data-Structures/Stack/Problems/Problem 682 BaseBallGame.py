'''Dekh ye Leetcode Ki problem 682 hai baseball game theek hai ab isme humein ek arry given hai 
operation karke theek hai ab isme values kuch aise hongi ["5","2","c","d","+"] theek hai ab isme actually mein
kya karna hai jyada kuch nahi humein ek record maintain karna hai aur vo record kuch aisa hoga 
jaise koi number aya like 5 aya toh record mein [5]= record save hogay 
                ab next 2 aya toh vo 5 ke sath chala gaya [5,2]=record 
                ab aya c iska matlab hai ki last jo bhi valid score tha usse remove kar do 
                                            like ab jo record hoga =[5] 2 remove ho gaya 
                ab aya d iska matlab jo last score the uska double record mein chala jayega 
                                            like aise [5,10]= record 
                ab aya + iska matlab jo bhi last record the unka sum record mein jud jayega 
                                            like that [5,10,15] aise 
ab ye dhyaan rahe ki pichla record remove nahi karna untill ye na kahe ki remove karne hai 
and final output jo hai record ke element ka sum hoga like
                5+10+15=30
output is 30
'''
'''
Derived Solution

isme simple stack ke operations lag rahe kaise :-
pahle hum ek stack name ka stack maintain karte hai =[]
ab jaise koi number aya toh vo kaise jayega like stack.append(int(operations))
and agar c aya toh simply stack.pop()
aur agar d aya toh simply stack.append(stack[-1]*2)
aur agar + aya toh simply stack.append(stack[-1]+stack[-2])
end sum(stack)
'''
class Solution:
    def Records(self,ops):
        stack = []
        for op in ops:
            if op =="+":
                stack.append(stack[-1]+stack[-2])
            elif op =="D":
                stack.append(stack[-1]*2)
            elif op =="C":
                stack.pop()
            else:
                stack.append(int(ops))
        return sum(stack)