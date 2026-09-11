from collections import deque
class Solution:
    def bfsOnGrid(self,grid:list[list[int]])->list[int]:
        grid=[
            [1,1,0],
            [1,0,0],
            [1,1,1]
        ]
        rows=len(grid)
        cols=len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        que=deque()
        visited=set() 
        que.append((0,0))
        visited.add((0,0))
        while que:
            r,c=que.popleft()
            print("Visiting",(r,c))
            for dr,dc in directions:
                nr=r+dr  
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if (nr,nc)not in visited:
                        visited.add((nr,nc))
                        que.append((nr,nc))