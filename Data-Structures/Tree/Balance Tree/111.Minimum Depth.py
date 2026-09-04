class Solution:
    def minDepth(self,root:list[int])->int:
        if root is None:
            return 0
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1+right
        if not root.right:
            return 1+left
        return 1+min(left,right)