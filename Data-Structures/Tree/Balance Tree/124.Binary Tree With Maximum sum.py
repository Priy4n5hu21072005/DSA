class Solution:
    def binaryTreeWithMaximumSum(self,root):
        self.ans=float('-inf')
        def dfs(node):
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            left=max(0,left)
            right=max(0,right)
            current_path=left+node.val+right
            self.ans=max(self.ans,current_path)
            return node.val+max(left,right)
        dfs(root)
        return self.ans