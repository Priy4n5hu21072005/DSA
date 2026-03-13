# Problem Name: Substring with Concatenation of All Words
# Problem Description: Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
def findSubstring(s,words):
    if not s or not words:
        return []
    word_len=len(words[0])
    word_count={}
    for w in words:
        word_count[w]=word_count.get(w,0)+1
    result=[]
    for i in range (word_len):
        l=i
        r=i
        count=0
        seen={}
        while r+word_len<=len(s):
            word=s[r:r+word_len]
            r +=word_len
            if word in word_count:
                seen[word]=seen.get(word,0)+1
                count +=1
                while seen[word]>word_count[word]:
                    l_word=s[l:l+word_len]
                    seen[l_word]-=1
                    l+=word_len
                    count-=1
                if  count==len(words):
                    result.append(l)
            else:
                seen.clear()
                count=0
                l=r
    return result
s="barfoothefoobarman"
words=["foo","bar"]
print(findSubstring(s,words))