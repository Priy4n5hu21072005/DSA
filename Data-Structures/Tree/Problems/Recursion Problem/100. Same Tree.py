class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def is_Same_Tree(self,p:list[TreeNode],q:list[TreeNode])->bool:
        # if dono Tree nahi hai toh bhi output true
        if not p and not q:
            return True
        # if dono mein se koi nahi hai tab
        if not p or not q:
            return False
        # ab Value
        if p.val != q.val:
            return False

        return self.is_Same_Tree(p.left,q.left) and self.is_Same_Tree(p.right,q.right)
    