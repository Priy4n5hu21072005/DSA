class Solution:
    def HappyNumber(self,n:int)->bool:

        seen = set() 

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            sum = 0

            while n >0:

                digit = n%10

                sum += digit*digit

                n=n//10

            n = sum
        return True
    
