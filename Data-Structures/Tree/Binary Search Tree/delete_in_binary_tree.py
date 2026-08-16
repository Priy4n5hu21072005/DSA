class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def delete(self,root:list[Node],key:int)->list[Node]:
        if root is None:
            return None
        if key< root.data:
            root.left=self.delete(root.left,key)
        elif key > root.data:
            root.right=self.delete(root.right,key)
        else:
            #Case 1 : with no childeren
            if root.left is None and root.right is None:
                return None
            #Case 2: With 1 childeren
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left  
            #Case 3 : with two children
            #inorder successor : right ka smallest element
            elif:
                successor=root.right
                while successor:
                    successor=successor.left  
                root.val=successor.val  
                root.right=self.delete(root.right,successor.val)

            # inorder preceder : left ka largest element
            else:
                preceder = root.left  
                while preceder:
                    preceder=preceder.right
                root.val=preceder.val  
                root.left=self.delete(root.left,preceder.val)
                
        return root