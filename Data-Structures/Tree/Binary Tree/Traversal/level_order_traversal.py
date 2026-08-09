class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def level_order(root,level,ans):
    if root is None:
        return
    if len(ans)<=level:
        ans.append([])
    ans[level].append(root.data)

    level_order(root.left,level+1,ans)
    level_order(root.right,level+1,ans)

def traversal(root):
    ans=[]
    traversal(root,0,ans)
    return ans
