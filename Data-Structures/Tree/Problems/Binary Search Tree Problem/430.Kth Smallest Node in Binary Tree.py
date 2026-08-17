class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def Kth_Smallest_Element(self,root:list[Node],k:int)->int:
        ans=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        return ans[k-1]