class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def search(self,root:list[Node],val:int)->list[Node]:
        if root is None:
            return None
        if root.val==val:
            return root
        if val<root.val:
            return self.search(root.left,val)
        return self.search(root.right,val)  
    