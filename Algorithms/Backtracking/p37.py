# Problem 37 : Sudoku Solver
class solution:
    def solveSudoku(self,brd):
        def isValid(rw,cl,vl):
            # Check row
            for i in range(9):
                if brd[rw][i]==vl:
                    return False
            # check column
            for i in range(9):
                if brd[i][cl]==vl:
                    return False
            # check 3*3 box
            box_row=3*(rw//3)
            box_col=3*(cl//3)

            # Traverse the box
            for row in range(3):
                for col in range(3):
                    if brd[box_row+row][box_col+col]==vl:
                        return False
            return True
        
        def solve():
            for rw in range(9):
                for cl in range(9):
                    if brd[rw][cl]=='.':
                        for vl in "123456789":
                            if isValid(rw,cl,vl):
                                brd[rw][cl]=vl
                                if solve():
                                    return True
                                brd[rw][cl]='.'
                        return False
            return True
        solve()

# test case
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s=solution()
s.solveSudoku(board)
for i in board:
    print(i)
