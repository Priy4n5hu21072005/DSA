'''
Humein ek String di hai s jisme sirf 3 he character hai a,b,c bus 
humein count karni hai kitni substring aise hai jisme teeno character aate hai 
maan lo ek string s = "abcabc"
an iske substring kuch aise honge 
"abc","abca","abcab","abcabc","bca","bcab","bcabc","cab","cabc","abc"
toh output ayega 10
'''
'''
Drived Solution
s="abcabc"
n=6
l=0
r=0
freq ={}
ans =0
'''
'''
step 1 : r =0
window = a
freq = a: 1,b:0,c:0 invalid , so r++
step 2 : r=1
window = ab
freq = a:1,b:1,c:0 invalid , so r++
step 3 : r=2
window = abc
freq = a:1,b:1,c:1 valid , 
ans += n-r
ans = 6-2 = 4

step 4: window shrink 
remove 'a'
l=1
...
'''

'''
psudo code 
l = 0 
ans = 0
for r in range((n)):
current += freq
while window is valid 
ans += n-r
left character ko freq se remove karo
l++
'''
class solution:
    def LongestSubstring(self,s):
        freq = {'a':0,'b':0,'c':0}
        l=0
        ans =0
        n = len(s)
        for r in range(n):
            freq[s[r]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                ans += n-r  
                freq[s[l]]-=1
                l+=1
        return ans 