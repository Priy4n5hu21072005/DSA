class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def Binary_Tree_Tilt(self,root:list[TreeNode])->int:
        tilt=0 
        def subtree_sum(node):
            nonlocal tilt
            left=subtree_sum(node.left)
            right=subtree_sum(node.right)
            tilt+=abs(left-right)
            return left+right+node.val 
        subtree_sum(root)
        return tilt
    