# This is the problem of Unique binary tree 
# humein n number diya hai humein 1 se n tak ke unique posssible  number of binary tree return karane hai 
class Treenode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution(object):
    def uniqueSolutionBinaryTree(self,n:int):
        def count(start,end):
            if start>end:
                return 1
            total=0
            for i in range (start,end+1):
                left=count(start,i-1)
                right=count(i+1,end)
                total += left*right
            return total
        return count(1,n)
    
n=3
obj=solution()
print(obj.uniqueSolutionBinaryTree(n))