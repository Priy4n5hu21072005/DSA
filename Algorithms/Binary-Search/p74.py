# Problem Name: Search a 2D Matrix
# Problem Description: Write an efficient algorithm that searches for a value target in an m x n integer matrix.
def searchTwoD(matrix,target):
    if not matrix or not matrix[0]:
        return False
    Rows=len(matrix)
    Columns=len(matrix[0])
    low=0
    high=Rows*Columns-1
    while low <= high:
        middle=(low+high)//2
        r=middle//Columns
        c=middle%Columns
        middle_value=matrix[r][c]
        if middle_value==target:
            return True 
        elif middle_value<target:
            low=middle+1
        else:
            high=middle-1
    return False
matrix=[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target=12
print(searchTwoD(matrix,target))
