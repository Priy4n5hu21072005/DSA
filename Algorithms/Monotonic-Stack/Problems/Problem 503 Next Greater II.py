'''
dekh ye problem same he pichle jaise par isme humein khali ek array given hai nums kar ke 
aur vo duplicate element exist karta hai and circular hai '''

class Sol:
    def NextGreaterElementII(self,nums):
        n = len(nums)
        stack =[]
        ans =[-1]*n 
        for i in range(2*n-1,-1,-1):
            real_idx = i%n  
            while stack and stack [-1] <= nums[real_idx]:
                stack.pop()
            if i < n :
                if stack :
                    ans[real_idx] = stack[-1]
            stack.append(nums[real_idx])
        return ans
    

'''                            Dry Run                                          '''
'''  
nums = [1,2,1]
n=3
stack =[]
ans =[-1,-1,-1]
for loop(5 to 0):
    i = 5
    real_idx = 2 
    while stack (condition fail)
    if 5<3(condition fail)
    stack =[1]
    
    i = 4
    real_idx = 1
    while stack (condition pass) and 1 <= 2 (condition pass):
        stack.pop(1) -> stack =[]
    if 4<3(condition fail)
    stack = [2]

    i = 3
    real idx = 0
    while stack(condition pass) and 2 <= 1(condition fail)
    if 3 < 3(condition fail)
    stack =[2,1]

    i = 2
    real idx = 2
    while stack(condition pass) ans 1 <= 1(condition pass):
    stack.pop(1) -> stack [2]
    while stack (condition pass) and 2<=1(condition fail)
    if 2 < 3(conditon pass):
        ans[2]=2  ans = [-1,-1,2]
    stack = [2,1]

    i = 1
    real_idx = 1
    while stack(condition pass) and 1 <= 2(condtion pass):
    stack.pop(1) -> stack =[2]
    while stack(condition pass) and 2 <= 2(conditon pass):
    stack =[]
    if 1 < 3:
    if stack(conditon fail):
    stack =[2]


    i = 0 
    real index = 0
    stack(condition pass) and 2 <= 1:
    
    if 0 < 3:
    if stack:
    ans[0] = 2
    ans = [1,1,2]

    stack=[2,1,1]

'''