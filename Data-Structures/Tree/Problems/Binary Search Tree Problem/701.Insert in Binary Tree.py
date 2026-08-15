class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def insertion(self,root:list[Node],val:int)->list[Node]:
        if root is None:
            return Node(val)
        if root.val > val :
            root.left=self.insertion(root.left,val)  
        else:
            root.right=self.insertion(root.right,val)
        return root
        