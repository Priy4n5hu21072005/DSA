'''
dekh isme humein 2 string given hai s and t simply dono type kar rahi hai characters ko aur inke pass hai 
    # ab jab bhi ye aye toh last type character delete ho jayega 
    for s = ab#c and t = ad#c
    toh s kaise process karega a
                               ab 
                               # remove last type character 
                               -> a 
                                ac
    aur t bhi same process karega toh uska last ac 
    ab dono same hai toh true ayega output
'''
'''
Derived Solution

hum ek build function bnyenge jaha build(s)==build(t) hai toh true
ab build function mein kya karenge 
like ek stack maintain karenge simply jo bhi normal alphabets hai toh stack mein push 
but # aya toh last character ko delete in case stack empty hai toh kuch nahi karna

'''
class Solution:
    def CompareStringAfterBackspace(self,s,t):
        def build(String):
            stack =[]
            for i in String:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build(s)==build(t)