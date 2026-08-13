class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def symmetry_tree(self,root:list[TreeNode])->bool:
        def mirror(leftSubtree,rightSubtree):
            if not leftSubtree and not rightSubtree:
                return True
            if not leftSubtree or not rightSubtree:
                return False
            if leftSubtree.val != rightSubtree.val:
                return False
            return mirror(leftSubtree.left,leftSubtree.right) and mirror(rightSubtree.left,rightSubtree.left)
        return mirror(root.left,root.right) 