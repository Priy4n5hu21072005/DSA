class sol:
    def SumSubarrayRange(self,nums):
        n = len(nums)
        def smallSubarray(nums):
            stack =[]
            l =[0]*n
            r=[0]*n
            
            # Previous Smaller
            for i in range(n):
                while stack and nums[stack[-1]]>nums[i]:
                    stack.pop()
                if stack:
                    l[i]=i-stack[-1]
                else:
                    l[i]=i+1
                stack.append(i)  
            stack.clear()

            # Next Smaller
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]>=nums[i]:
                    stack.pop()
                if stack:
                    r[i]=stack[-1]-i 
                else:
                    r[i]=n-i
                stack.append(i)  
            stack.clear()

            # final contri 
            ans = 0
            for i in range(n):
                ans+=nums[i]*l[i]*r[i]
            return ans  
        
        def largeSubarray(nums):
            stack =[]
            l=[0]*n
            r=[0]*n

            #previous greater
            for i in range(n):
                while stack and nums[stack[-1]]<nums[i]:
                    stack.pop()
                if stack:
                    l[i]=i-stack[-1]
                else:
                    l[i]=i+1
                stack.append(i)
            stack.clear()

            # Next Greater
            for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]]<=nums[i]:
                    stack.pop()
                if stack:
                    r[i]=stack[-1]-i
                else:
                    r[i]=n-i   
                stack.append(i)   
            stack.clear()

            ans = 0
            for i in range(n):
                ans += nums[i] * l[i] * r[i]
            return ans   
        return largeSubarray(nums)-smallSubarray(nums) 