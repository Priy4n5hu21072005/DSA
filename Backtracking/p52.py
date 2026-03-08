# This is the problme NQueen II and this problem just return the number of solution 
class solution:
    def nqueenII(self,n:int):
        cols=set() # occupied columns
        dig1=set() # row-col
        dig2=set() # row+col
        def back(row):
            if row==n:
                return 1
            total=0
            for c in range(n):
                if c in cols or row-c in dig1 or row+c in dig2:
                    continue
                cols.add(c)
                dig1.add(row-c)
                dig2.add(row+c)
                total+=back(row+1)
                cols.remove(c)
                dig1.remove(row-c)
                dig2.remove(row+c)
            return total
        return back(0)
