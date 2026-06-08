class Solution:
    def Reverse(self,s):
        temp = s[::-1]
        for i in range (len(s)):
            s[i]=temp[i]
        return s
s = ['h','e','l','l','o']
obj = Solution()
print(obj.Reverse(s))