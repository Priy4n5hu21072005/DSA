class Solution1:
    def Valid(self,s):
        if not s :
            return False
        temp=""
        for char in s:
            if char.isalnum():
                temp+=char.lower()
        return temp==temp[::-1]
class Solution2:
    def Valid(self,s):
        temp=""
        for ch in s:
            if ch.isalnum():
                temp+=ch.lower()
        rev=""
        for i in range(len(temp)-1,-1,-1):
            rev+=temp[i]
        return temp==rev
class Solution3:
    def Valid(self,s):
        l=0
        r=len(s)-1 
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
obj = Solution1()
obj2 = Solution2()
obj3=Solution3()
s = "A man, a plan, a canal: Panama"
print(obj.Valid(s))
print(obj2.Valid(s))
print(obj3.Valid(s))