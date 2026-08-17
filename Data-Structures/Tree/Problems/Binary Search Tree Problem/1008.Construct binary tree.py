class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def Construct_Binary_Tree_Using_Preorder(self,preorder:list[TreeNode])->list[TreeNode]:
        i=0
        def build(boundary):
            nonlocal i
            if i == len(preorder) or preorder[i]>boundary:
                return None
            root=TreeNode(preorder[i])
            i+=1
            root.left=build(root.val)
            root.right=build(boundary)
            return root
        return build(float('inf'))