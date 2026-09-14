from collections import deque
class Solution:
    def shortest_path_in_a_matrix(grid):
        n=len(grid)
        qu=deque()
# 1. Start and destination valid
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
# 2. Queue mein (row,col,distance) ko daalenge
        qu.append((0,0,1))
        grid[0][0]=1
        directions=[(-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]
# 3. BFS 
        while qu:
            r,c,distance=qu.popleft()
# 6.aur answer destination par hai toh mil gaya answer
            if r==n-1 and c==n-1:
                return distance
# 4. 8 neighbour ko check karna 
            for dr,dc in directions:
                if 0<=r+dr<n and 0<=c+dc<n:
                    if grid[r+dr][c+dc]==0:
                        grid[r+dr][c+dc]=1
# 5. agar valid hai unvisited hai toh simply queue
                        qu.append((r+dr,c+dc,distance+1))
        return -1


