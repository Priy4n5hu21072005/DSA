'''
same question hai remove adjucent duplicate character jaise he but ek bas change hai uss question saare lower letter the
isme kuch lower kuch upper hai toh bus little bit change aya
'''
class solution:
    def MakeStringGreat(self,s):
        stack = []
        for ch in s:
            if stack and stack[-1]!=ch and stack[-1].lower()==ch.lower():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)