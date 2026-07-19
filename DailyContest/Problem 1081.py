class Solution:
    def SmallSubSequence(self,s:str)-> str:
        last={ch:i for i,ch in enumerate(s)}
        stack =[]
        visted =set()
        for i, ch in enumerate(s):
            if ch in visted:
                continue
            while (stack and stack[-1]>ch and last[stack[-1]]>i):
                visted.remove(stack.pop())
            stack.append(ch)
            visted.add(ch)  
        return "".join(stack)

s = "bcabcb"
obj1 = Solution()
print(obj1.SmallSubSequence(s))