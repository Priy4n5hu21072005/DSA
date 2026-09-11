from collections import deque
from typing import List
class solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        og_color=image[sr][sc]
        if og_color==color:
            return image
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        que=deque()
        que.append((sr,sc))
        image[sr][sc]=color
        while que:
            r,c=que.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if image[nr][nc]==og_color:
                        image[nr][nc] =color
                        que.append((nr,nc))
        return image