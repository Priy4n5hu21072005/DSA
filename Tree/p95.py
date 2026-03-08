# This is the problem of Unique binary tree 
# humein n number diya hai humein 1 se n tak ke unique posssible binary tree return karane hai 
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution(object):
    def uniqueBinaryTree(self,n):
        if n==0:
            return []
        def build(start,end):
            if start>end:
                return [None]
            tree=[]
            for i in range(start,end+1):
                l_tree=build(start,i-1)
                r_tree=build(i+1,end)
                for l in l_tree:
                    for r in r_tree:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        tree.append(root)
            return tree
        return build(1,n)
n=3
obj=solution()
print(obj.uniqueBinaryTree(n))
