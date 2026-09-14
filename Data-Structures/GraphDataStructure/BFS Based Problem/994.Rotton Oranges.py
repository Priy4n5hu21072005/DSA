from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        que=deque()
        fresh=0
        minutes=0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    que.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        while que and fresh>0:
            size=len(que)
            for _ in range(size):
                r,c=que.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc

                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            fresh-=1
                            que.append((nr,nc))
                minutes+=1
            if fresh>0:
                return -1
        return minutes
