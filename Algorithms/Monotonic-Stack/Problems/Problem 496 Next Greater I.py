'''
Do array given hai nums1 and nums2
aur vo kuch aise diye honege nums1 = [4,1,2] and nums2 = [3,4,1,2]
ab humein nums1 ke element ka next greater element nikalna hai theek hai in nums2 
ab ye next greater element kya hai dekh ye jyda kuch nahi hai right side se dekhni koi next value kiya given 
element se badi hai ki nahi bas 
for example nums1 ka pahla element 4 hai ab ye nums2 mein kaha pe hai 1 index pe ab iske right mein koi 
iss se badi value hai nahi toh return -1

ab hum ne isme stack kyu use kya because jo stack hai vo he latest unresolved value ko store karta hai 
'''

'''algorithm
stack =[]
freq = {}
for n in nums2:
    while stack and stack [-1]<n:
        freq[stack.pop()]=n
    stack.append(n)
ans =[]
for n in nums1:
    ans.append(freq.get(n,-1))'''

class Solution:
    def NextGreaterElementI(self,nums1,nums2):
        stack =[]
        freq ={}
        for i in nums2:
            while stack and stack[-1]<i:
                freq[stack.pop()]=i
            stack.append(i)  
        ans =[]
        for i in nums1:
            ans.append(freq.get(i,-1))
        return ans 

n1 =[4,1,2]
n2=[1,3,4,2]
object=Solution()
print(object.NextGreaterElementI(n1,n2))