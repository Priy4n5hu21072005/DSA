class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def balance_binary_search_tree(root:list[int])->list[int]:
    value=[]
    def inorder(node):
        if node is None:
            return
        nonlocal value
        inorder(node.left)
        value.append(node.val)
        inorder(node.right)

    inorder(root)


    def build(left,right):
        if left>right:
            return None
        mid=(left+right)//2

        node=Node(value[mid])

        node.left=build(left,mid-1)
        node.right=build(mid+1,right)

        return node
    return build(0,len(value)-1)

        
