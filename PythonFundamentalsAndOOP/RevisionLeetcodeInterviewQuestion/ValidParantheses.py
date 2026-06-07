class Solution1:
    def Valid(self,s):
        if not s :
            return False
        while "[]" in s or "()" in s or "{}" in s :
            s=s.replace("[]", "")
            s=s.replace("{}", "")
            s=s.replace("()", "")
            
        return s ==""
s=""
obj=Solution1()
print(obj.Valid(s))

class Solution2:
    def valid(self,s):
        stack=[]
        mapping={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in "({[":
                stack.append(char)
            else :
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return len(stack)==0