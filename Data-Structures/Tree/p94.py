# Problem Name: Binary Tree Inorder Traversal
# Problem Description: Return the inorder traversal of a binary tree's nodes' values.
class NodeRoot(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution(object):
    def inorderTraverse(self,root):
        res=[]
        def inorder(node):
            if not node :
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res
    

        
