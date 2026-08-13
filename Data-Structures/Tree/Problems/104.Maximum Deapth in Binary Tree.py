class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def maxDeapth(self,root:list[TreeNode])->int:
        # Base Case
        if root is None:
            return
        # left subtree traverse
        left = self.maxDeapth(root.left)

        #right subtree traverse
        right = self.maxDeapth(root.right)

        # Maximum answer
        return 1 + max(left,right)
    