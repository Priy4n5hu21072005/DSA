# Problem Name: Repeated DNA Sequences
# Problem Description: Find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
def repSeq(s):
    if len(s)<10:
        return[]
    seen=set()
    repeated =set()
    for i in range (len(s)-9):
        sub=s[i:i+10]
        if sub in seen :
            repeated.add(sub)
        else:
            seen.add(sub)
    return list(repeated)
s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(repSeq(s))