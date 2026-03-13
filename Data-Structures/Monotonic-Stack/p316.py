# Problem Name: Remove Duplicate Letters
# Problem Description: Remove duplicate letters so that every letter appears once and only once. Result must be the smallest in lexicographical order.
def removeDuplicate(s):
    last={}
    for i,ch in enumerate(s):
        last[ch]=i
    stack=[]
    seen=set()
    for i,ch in enumerate(s):
        if ch in seen:
            continue
        while stack and ch<stack[-1] and last[stack[-1]]>i:
            seen.remove[stack.pop()]
        stack.append(ch)
        seen.add(ch)
    return "".join(stack)
