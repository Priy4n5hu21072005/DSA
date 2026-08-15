class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def univalued_binary_tree(self,root:list[TreeNode])->int:
        ans=0
        def longest(node):
            nonlocal ans
            if not node:
                return 0
            left=longest(node.left)
            right=longest(node.right)
            if node.left and node.left.val==node.val:
                left+=1
            else:
                left=0
            if node.right and node.right.val==node.val:
                right+=1
            else:
                right=0
            ans=max(ans,left+right)
            return max(left,right)
        longest(root)
        return ans