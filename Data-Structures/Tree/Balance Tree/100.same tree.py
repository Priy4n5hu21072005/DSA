class Solution:
    def same_tree(self,p,q)->bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.same_tree(p.left,q.left)and self.same_tree(p.right,q.right)
