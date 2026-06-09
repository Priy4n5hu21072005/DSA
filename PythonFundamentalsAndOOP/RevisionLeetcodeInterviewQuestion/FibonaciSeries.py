# Iterative Method 
class Solution1:
    def FibonaciSeries(self,n):
        a = 0 # fib(0) =0
        b = 1 # fib(1) = 1
        #for i in range(n)):
            #print(a,end=" ")
        for i in range(2,n+1):
            c = a+b
            a=b 
            b=c 
        return b

n = int(input("Enter the number"))
obj = Solution1()
obj.FibonaciSeries(n)

# Recursive Approach
class Solution2:
    def FibonaciSeries(self,n):
        if n <=1:
            return n   
        return self.FibonaciSeries(n-1) + self.FibonaciSeries(n-2)
n = int(input())
obj = Solution2()
obj.FibonaciSeries(n)