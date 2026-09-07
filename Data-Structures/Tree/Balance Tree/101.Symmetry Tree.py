class Solution:
    def isSymmetryTree(self,root)->bool:
        if root is None:
            return None
        def mirror(left_subtree,right_subtree):
            if not left_subtree and not right_subtree:
                return True
            if not left_subtree or not right_subtree:
                return False
            if left_subtree.val!=right_subtree.val:
                return False
            return(mirror(left_subtree.left,right_subtree.right)and mirror(left_subtree.right,right_subtree.left))
        return mirror(root.left,root.right)