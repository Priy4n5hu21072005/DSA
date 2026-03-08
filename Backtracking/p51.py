# This is the problem of N-Queen 
class solution:
    def nqueen(self,n:int):
        board=[["."]*n for _ in range(n)]
        r=[]
        cols=set() # occupied columns
        dig1=set() # row-col
        dig2=set() # row+col
        def back(row):
            if row==n:
                r.append(["".join(r)for r in board]) # queen ko place bta raha hai
                return
            for col in range(n):
                if col in cols or row-col in dig1 or row+col in dig2:
                    continue
                board[row][col]="Q" # queen ko place kar raha hai 
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)
                back(row+1)
                board[row][col]="." # remove karke backtrack karne mein help kar raha hai 
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        back(0)
        return r
n=4
obj=solution()
print(obj.nqueen(n))
