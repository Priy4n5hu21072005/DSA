# Problem 438 : Find All Anagrams in a String
# Input : s = "cbaebabacd", p = "abc"
# Output : [0,6]
class Solution(object):
    def FindAnagram(self,s,p):
        if len(p)>len(s):
            return []
        window=[0]*26
        p_count=[0]*26
        for ch in p:
            p_count[ord(ch)-ord('a')]+=1
        res=[]
        for i in range(len(s)):
            window[ord(s[i])-ord('a')]+=1
            if i>=len(p):
                window[ord(s[i-len(p)])-ord('a')]-=1
            if window==p_count:
                res.append(i-len(p)+1)
        return res

s="cbaebabacd"
p="abc"
print(Solution().FindAnagram(s,p))
