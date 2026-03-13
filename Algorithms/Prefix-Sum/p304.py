# Problem Name: Range Sum Query 2D - Immutable
# Problem Description: Calculate the sum of the elements of matrix inside a defined rectangle.
class solution(object):
    def __init__(self,matrix):
        if not matrix or not matrix[0]:
            self.prefix=[]
            return
        rows,cols=len(matrix),len(matrix[0])
        self.prefix=[[0]*(cols+1) for _ in range (rows+1)]
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                self.prefix[i][j]=(
                    matrix[i-1][j-1]
                    + self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1]
                )
    def sumRegion(self,row1,col1,row2,col2):
        return(
            self.prefix[row2+1][col2+1]
            - self.prefix[row1][col2+1]
            - self.prefix[row2+1][col1]
            + self.prefix[row1][col1]
        )
matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
obj=solution(matrix)
print(obj.sumRegion(1,1,2,2))