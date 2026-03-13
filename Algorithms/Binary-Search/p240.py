# Problem Name: Search a 2D Matrix II
# Problem Description: Search for a value target in an m x n integer matrix where rows and columns are sorted.
def searchinMatrix(matrix,target):
    if not matrix or not matrix[0]:
        return False
    Rows=len(matrix)
    Columns=len(matrix[0])
    row=0
    col=Columns-1
    while row<Rows and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            c-=1
        else:
            r+=1
    return False