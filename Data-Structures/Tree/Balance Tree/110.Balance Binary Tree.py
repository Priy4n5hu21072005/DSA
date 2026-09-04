class Solution:
    def balance_binary_tree(self,root:list[int])->bool:
        def heightDifference(node):
            if node is None:
                return 0
            left=heightDifference(node.left)
            right=heightDifference(node.right)
            if left==-1:
                return -1
            if right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return heightDifference(root)!=-1
    
            