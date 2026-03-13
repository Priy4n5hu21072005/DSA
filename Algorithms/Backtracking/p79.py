# Problem Name: Word Search
# Problem Description: Given an m x n grid of characters board and a string word, return true if word exists in the grid.
class solution:
    def wordSearch(self,words:str,board):
        rows=len(board)
        cols=len(board[0])
        def back(i,j,ind):
            if ind == len(words):
                return True
            if (i < 0 or j < 0 or i >= rows or j >= cols or board[i][j]!=words[ind]):
                return False
            temp=board[i][j]
            board[i][j]="*"
            result=(
                back(i+1,j,ind+1) or
                back(i-1,j,ind+1) or
                back(i,j+1,ind+1) or
                back(i,j-1,ind+1)
            )
            board[i][j]=temp
            return result
        for i in range(rows):
            for j in range(cols):
                if back(i,j,0):
                    return True
        return False
words="ABCCED"
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
obj=solution()
print(obj.wordSearch(words,board))