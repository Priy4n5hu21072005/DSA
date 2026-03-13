# Problem Name: Validate Binary Search Tree
# Problem Description: Determine if a binary tree is a valid binary search tree (BST).
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution(object):
    def IsValidBST(self,root):
        def validate(node,low,high):
            if not node:
                return True
            if node.val <= low or node.val>=high:
                return False
            left_check=validate(node.left,low,node.val)
            right_check=validate(node.right,node.val,high)
            return left_check and right_check
        return validate(root,float('-inf'),float('inf'))
