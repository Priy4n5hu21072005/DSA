# Problem Name: Path Sum
# Problem Description: Return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
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
        