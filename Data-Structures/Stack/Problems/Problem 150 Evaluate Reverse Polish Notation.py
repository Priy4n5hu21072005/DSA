'''
Problem mein humein ek token naam ka array given hai aur uss array mein humein numbers and operator dono
 given hai ab humein usme reverse polish notation karna hai 
 ab ye reverse polish notation kis chidya ka naam hai vo bta ta hun 
 dekh isme humein kuch aise expression dene hai 2 1 +(postfix)
                                                normal expression kuch aise hote hai 2+1 but rpn(postfix) aise hoti
for example token = [2,1,+,3,*]
ab iska kaise solve karenge toh ye hoga kuch aise pahle ((2+1)*3)
'''
'''
ab isse hum stack se solve karenge because humein last 2 numbers pe operation perform karna hai 
lekin ek aur condition di hai leetcode ke problem mein 
sab se pahle 5//2 toh 2 hota hai but -5//2 hota hai -3 isliye hum int(-5/2)=-2 because trancuate towards zero '''

class Solution:
    def PerformRPN(self,token):
        stack =[]
        operations ={
            "+":lambda a,b:a+b, 
            "-":lambda a,b:a-b,
            "*":lambda a,b:a*b,
            "/":lambda a,b:int(a/b)
        }
        for t in token:
            if t in operations:
                b=stack.pop()
                a=stack.pop()
                stack.append(operations([token](a,b)))
            else:
                stack.append(int(t))
        return stack[-1]