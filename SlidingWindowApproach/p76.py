def minSubString(s,t):
    if not s or not t:
        return ""
    need={}
    for n in t:
        need[n]=need.get(n,0)+1
    win={}
    have=0
    need_count=len(need)
    ans=[-1,-1]
    Length_ans=float('inf')
    l=0
    for r in range(len(s)):
        n=s[r]
        win[n]=win.get(n,0)+1
        if n in need and need[n]==win[n]:
            have +=1
        while have==need_count:
            if (r-l+1)<Length_ans:
                ans=[l,r]
                Length_ans=r-l+1
            win[s[l]]-=1
            if s[l] in need and need[s[l]]>win[s[l]]:
                have -=1
            l+=1
    l,r=ans
    return "" if Length_ans==float('inf') else s[l:r+1]
s="ADOBECODEBANC"
t="ABC"
print(minSubString(s,t))
