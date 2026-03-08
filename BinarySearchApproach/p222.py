# This is the count the number of nodes in tree
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def countNode(root):
    if not root:
        return 0
    height=0
    current=root
    while current.left:
        height+=1
        current=current.left
    def nodeExist(index,height,node):
        left=0
        right=(1<<height)-1
        for _ in range (height):
            mid=(left+right)//2
            if index<=mid:
                node=node.left
                right=mid
            else:
                node=node.right
                left=mid+1
            if not node:
                return False
        return True
    low=0
    high=(1<<height)-1
    lastNode=0
    while low <= high:
        mid=(low+high)//2
        if nodeExist(mid,height,root):
            lastNode=mid+1
            low=mid+1
        else:
            high=mid-1
    return (1<<height)-1+lastNode
# Tree:
#        1
#       / \
#      2   3
#     / \  /
#    4  5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(countNode(root))




