class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def Path_Sum_II(self,root:list[TreeNode],targetSum)->list[list[int]]:
        path=[]
        result =[]
        def dfs(node,remaining):
            if node is None:
                return 
            path.append(node.val)
            remaining-=node.val  

            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path.copy())

            dfs(node.left,remaining)
            dfs(node.right,remaining)
            path.pop()
        dfs(root,targetSum)
        return result
