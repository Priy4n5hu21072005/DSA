class Solution:
    def decodeString(self,s):
        stack =[]
        current =""
        number = 0 
        for i in s:
            if i.isdigit():
                number = number*10 +int(i)  
            elif i =="[":
                stack.append((number,current))
                number =0
                current =""
            elif i.isalpha():
                current +=i
            elif i =="]":
                rep,pre =stack.pop()
                current = pre + current*rep
        return current