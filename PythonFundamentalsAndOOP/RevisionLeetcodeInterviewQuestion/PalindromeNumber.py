class Solution:
    def PalindromeNumber(self,x):
        rev = 0
        while x > 0 :
            dg = x % 10
            rev = rev *10 + dg
            x //=10
        return x == rev
