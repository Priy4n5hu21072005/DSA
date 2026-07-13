from collections import deque
class sol:
    def Problem994(self,grid):
        rows =len(grid)
        cols = len(grid[0])
        qu=deque()
        fresh =0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    qu.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        min =0
        dir =[(1,0),(-1,0),(0,1),(0,-1)]

        while qu and fresh > 0:
            size = len(qu)
            for _ in range(size):
                r,c=qu.popleft()

                for dr,dc in dir:
                    nr = r+dr
                    nc =c+dc
                    if (0<=nr<rows and 0 <=nc<cols and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        qu.append((nr,nc))

            min +=1
        return min if fresh==0 else -1
