class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left  
        self.right=right

class Solution:
    def min_value(self,root):
        if root is None:
            return -1
        current=root
        while current.left :
            current=current.left
        return current.val         

    def max_value(self,root):
        if root is None:
            return -1
        current=root
        while current.right:
            current=current.right
        return current.val     