'''
maan lete hai ki humare pass ek file system hai theek hai 
ab hum starting mein hai main folder pe toh humare pass 3 commands hai 
1. "x/" -> ye command se parent folder se child folder mein jana hai 
2. "../" -> agar child folder mein ho toh parent mein jao aur agar parent mein he ho toh bo he raho 
3. "./" -> jis folder mein ho udhar he raho 
'''
'''
for example logs = ["d1/","d2/","../","./"]
start deapth = 0
step 1 d1/ -> child folder mein jao deapth = 1
step 2 d2/ -> child folder mein jao deapth = 2
step 3 ../ -> parent folder mein vapas deapth = 1
step 4 ./ -> jaha ho vahi raho toh deapth = 1
'''
class Solution:
    def LogFolder(self,logs):
        stack = []
        for l in logs :
            if l == "../":
                if stack:
                    stack.pop()
            elif l == "./":
                continue
            else:
                stack.append(l)
        return len(stack)