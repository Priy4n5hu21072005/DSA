class TreeNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val

firstNode=TreeNode(4)
secondNode=TreeNode(14)
thirdNode=TreeNode(15)
fourthNode=TreeNode(16)

firstNode.left=secondNode
firstNode.right=thirdNode
secondNode.left=fourthNode
