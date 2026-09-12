from collections import deque
class Solution:
    def maxAreaLand(grid:list[list[int]])->int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        max_area=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    area=0 
                    qu=deque()
                    qu.append((r,c))
                    grid[r][c]="0"
                    while qu:
                        cr,cc=qu.popleft()
                        area+=1
                        for dr,dc in directions:
                            nr=dr+cr
                            nc=dc+cc
                            if 0<=nr<rows and 0<=nc<cols:
                                if grid[nr][nc]=="1":
                                    grid[nr][nc]="0"
                                    qu.append((nr,nc))
                    max_area=max(max_area,area)  
        return max_area               