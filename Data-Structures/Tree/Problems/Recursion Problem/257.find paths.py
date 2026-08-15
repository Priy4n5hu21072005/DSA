class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def paths(self,root:list[TreeNode])->list[str]:
        ans=[]

        def dfs(node,path):
            if node is None:
                return 
            path.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append("->".join(path))
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        dfs(root,[])
        return ans
