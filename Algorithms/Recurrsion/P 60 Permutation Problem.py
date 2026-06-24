class Solution:
    def Permutation(self,n,k):
        used = [False]*(n+1)
        self.count = 0
        self.ans = ""
        def solve(path):
            if self.ans != "":
                return
            # Base Case
            if len(path)==n:
                self.count +=1
                if self.count == k:
                    self.ans = path
                return
            # Traverse
            for num in range(1,n+1):
                if not used[num]:
                    used[num]=True
                    solve(path+str(num))
                    used[num]=False
        solve("")
        return self.ans

n = 3
k = 4
object=Solution()
print(object.Permutation(n,k))