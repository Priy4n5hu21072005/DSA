'''
Problem 1967 mein humein ek pattern name ka string array given hai and word name ka ek string di hai 
ab humein jo word diya hai uska substring dekhna hai ki vo pattern mein kitni baar appear hua hai 
for example 
pattern = ["a","abc","bc","d] and word = "abc"
output = 3
because "a" is the substring of word="abc" and appear in pattern so count = 1
similarly "abc" is also the substring then count = 2
and "bc" is also the substring then count = 3
but "d" is not the substring of word so not included so the final output is 3
'''
'''
Drived Solution
count = 0
for every character in pattern:
        if word in pattern:
                count +=1
return count 

time complexity is O(n*m*k) where n = lenght(pattern),
                                  m = length(word),
                                  k = length(every word in pattern)
'''
class Solution:
    def SubstringCount(self,patterns,word):
        count = 0
        for i in patterns:
            if i in word:
                count +=1
        return count

pattern = ["a","abc","bc","d"]
word ="abc"
object = Solution()
print(object.SubstringCount(pattern,word))