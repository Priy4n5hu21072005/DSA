class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Insert_Operation:
    def insert_operation(self,root,key):
        if root is None:
            return TreeNode(key)
        if key<root.val:
            root.left=self.insert_operation(root.val,key)
        else:
            root.right=self.insert_operation(root.val,key)
        return root