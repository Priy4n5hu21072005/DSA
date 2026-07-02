'''
Humein ek string di gai hai s humein simply aur kuch nahi karna adjecent duplicated element ko remove karna hai 
for example s = abbaca -> aaca -> ca output -> ca hoga 
'''
'''
Derived Solution 
ek stack bnyenge aur har values ko usme store karenge aur ye dekhenge ki current character and top elemnt same 
hai ki nahi like kuch aise 
stack = []
s = abbaca
current character a , stack = [a]
now = b , stack = [ab]
now b , stack [a] b remove
now a , stack =[] a remove
now c , stack =[c]
now a , stack =[ca]

'''

class Solution:
    def RemoveAdjucent(self,s):
        stack =[]
        for i in s :
            if stack and stack[-1]==i: 
                stack.pop()
            else:
                stack.append(i)  
        return "".join(stack)