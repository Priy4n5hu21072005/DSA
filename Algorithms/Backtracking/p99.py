# Problem Name: Recover Binary Search Tree
# Problem Description: Recover the binary search tree where two nodes were swapped by mistake.
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class solution(object):
    def RecoveryBST(self,root):
        self.prev=None
        self.first=None
        self.second=None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val>node.val:
                if not self.first:
                    self.first=self.prev
                self.second=node
            self.prev=node
            inorder(node.right)
        inorder(root)
        self.first.val,self.second.val=self.second.val,self.first.val