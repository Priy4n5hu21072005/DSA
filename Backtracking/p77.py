# This is the combination problme humein n , k do integer diye hai aur humein return karana hai combination k with range [1,n]
class solution:
    def combination(self,n,k):
        res=[]
        curr=[]
        def back(start):
            if len(curr)==k:
                res.append(curr[:])
                return
            for i in range(start , n+1):
                curr.append(i)
                back(i+1)
                curr.pop()
        back(1)
        return res
n,k=4,2
obj=solution()
print(obj.combination(n,k))