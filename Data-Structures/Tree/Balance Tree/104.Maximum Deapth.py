class Solution:
    def maximumDeapth(self,root:list[int])->int:
        if root is None:
            return 0
        left = self.maximumDeapth(root.left)
        right=self.maximumDeapth(root.right)
        return 1+max(left,right)