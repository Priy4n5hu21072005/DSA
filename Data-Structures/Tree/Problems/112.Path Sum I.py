class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def Path_Sum_I(self,root:list[TreeNode],targetSum:int)->bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        targetSum -= root.val  
        return (self.Path_Sum_I(root.left,targetSum) or self.Path_Sum_I(root.right,targetSum))

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum=22
object = Solution()
print(object.Path_Sum_I(root,targetSum))
