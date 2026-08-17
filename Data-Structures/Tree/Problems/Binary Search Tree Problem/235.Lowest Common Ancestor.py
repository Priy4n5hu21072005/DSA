class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def Lowest_Common_Ancestor(self,root:list[Node],p:Node,q:Node)->Node:
        while root:
            if p<root.val and q<root.val:
                root=root.left  
            elif p>root.val and q>root.left:
                root=root.right
            else:
                return root
        
        