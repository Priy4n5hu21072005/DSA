# This is the problem where we Longest Substring with At Least K Repeating Characters
# Brute Force
def longestSubstring(s,k):
    n=len(s)
    ans=0
    for i in range (n):
        freq={}
        for j in range (i,n):
            ch=s[j]
            freq[ch]=freq.get(ch,0)+1
            valid = True
            for value in freq.values():
                if value <k:
                    valid = False
                    break
            if valid:
                ans=max(ans,j-i+1)
    return ans
s = "aaabb"
k = 3
print(longestSubstring(s,k))


