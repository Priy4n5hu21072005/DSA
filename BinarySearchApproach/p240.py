# This is the problme of search in 2D matrix II
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