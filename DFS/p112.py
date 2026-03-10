# This is the problem 112 of leetcode 
# in this problem we have a binary tree and targetsum value we just need to check that from the root to leaf 
# the sum is equal to the path or not 
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def hasPath(self,root,targetSum):
        if not root :
            return False
        if not root.left and not root.right:
            return targetSum==root.val
        targetSum-=root.val
        return (self.hasPath(root.left,targetSum)) or (self.hasPath(root.right,targetSum))
        