from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    que=deque()
                    que.append((r,c))
                    grid[r][c]="0"
                    while que:
                        cr,cc=que.popleft()
                        for dr,dc in directions:
                            nr=cr+dr
                            nc=dc+cc
                            if 0<=nr<rows and 0<=nc<cols:
                                if grid[nr][nc]=="1":
                                    grid[nr][nc]="0"
                                    que.append((nr,nc))
        return islands
