# This is the problem 402 Remove K digits 
def removeKdigits(num,k):
    if k >=len(num):
        return "0"
    stack=[]
    for i in range(len(num)):
        while stack and stack[-1]>num[i] and k>0:
            stack.pop()
            k-=1
        stack.append(num[i])
    while k >0:
        stack.pop()
        k-=1
    result="".join(stack)
    result=result.lstrip("0")
    return result if result else 0

num = "1432219"
k = 3
print(removeKdigits(num,k))