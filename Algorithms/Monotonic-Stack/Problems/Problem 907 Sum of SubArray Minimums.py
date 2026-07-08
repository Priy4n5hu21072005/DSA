class Sol:
    def Problem907(self,nums):
        stack =[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > i:
                stack.pop()
            if stack:
                left=stack.append(nums[stack[-1]])
            stack.append(i)

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]>=i: 
                stack.pop()
            if stack:
                right = stack.append(nums[stack[-1]])
            stack.append(i)  
        contributions = left * right
        
