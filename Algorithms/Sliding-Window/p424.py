# Problem Name: Longest Repeating Character Replacement
# Problem Description: Return the length of the longest substring containing the same letter after replacing at most k characters.
def replaceKlatter(s,k):
    n=len(s)
    freq={}
    l=0
    r=0
    ans=0
    max_freq=0
    for r in range (n):
        ch=s[r]
        freq[ch]=freq.get(ch,0)+1
        max_freq=max(freq.values())
        length=r-l+1
        while length-max_freq>k:
            freq[s[l]]-=1
            l+=1
        ans=max(ans,length)
    return ans
s = "ABAB"
k = 2
print(replaceKlatter(s,k))