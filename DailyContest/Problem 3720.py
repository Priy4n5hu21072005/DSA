'''
1. target ko left → right follow karo
2. Jab possible ho, same character choose karo
3. Agar same character nahi milta:
      available characters mein target se bada smallest character choose karo
      baaki characters ascending order mein laga do
4. Agar same character milta raha aur end tak pahunch gaye:
      target ke equal ban gaya
      ab right se backtrack karo
      kisi position par slightly bigger character choose karo
5. Agar kahin bhi bigger character nahi mila:
      return 

'''

from collections import Counter
class Solution:
    def lexGreaterPermutation(self,s:str,target:str)->str:
        n= len(s)
        count=Counter(s)
        def solve(i):
            if i==n:
                return None
            ch=target[i]
            if count[ch]>0:
                count[ch]-=1
                result=solve(i+1)
                count[ch]+=1
                if result is not None:
                    return ch+result
            for c in range(ord(ch)+1,ord('z')+1):
                bigger=chr(c)
                if count[bigger]>0:
                    count[bigger]-=1
                    suffix=""
                    for x in range(ord('a')+1,ord('z')+1):
                        suffix+=chr(x)*count[chr(x)]
                    count[bigger]+=1
                    return bigger+suffix
            return None
        ans=solve(0)
        return ans if ans is not None else ""