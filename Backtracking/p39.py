# This is the problem for combination sum using backtracking
def combinationSum(candidate,target):
    result=[]
    current=[]
    def backtrack(start,remaning):
        if remaning==0:
            result.append(current[:])
            return 
        if remaning<0:
            return
        for i in range(start,len(candidate)):
            current.append(candidate[i])
            backtrack(i,remaning-candidate[i])
            current.pop()
    backtrack(0,target)
    return result
candidate = [2,3,6,7]
target = 7
print(combinationSum(candidate,target))