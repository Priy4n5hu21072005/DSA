# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightDifference(node):
            if node is None:
                return 0
            left=heightDifference(node.left)
            right=heightDifference(node.right)
            if left==-1:
                return -1
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return heightDifference(root)!=-1
            