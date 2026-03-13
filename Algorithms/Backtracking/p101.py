# Problem Name: Symmetric Tree
# Problem Description: Check whether a binary tree is a mirror of itself.
class TreenNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def IsSymmetry(self,r):
        def mirror(l,r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return mirror(l.left,r.right) and mirror(l.right,r.left)
        return mirror(r.left,r.right)