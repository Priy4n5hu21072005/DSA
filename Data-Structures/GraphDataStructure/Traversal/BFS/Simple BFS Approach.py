from collections import deque
class solution:
    def bfs(adj:list[list[int]])->list[int]:
        v=len(adj)
        visited=[False]*v
        res=[]
        src=0
        qu=deque()
        visited[src]=True
        qu.append(src)
        while qu:
            current=qu.popleft()
            res.append(current)
            for x in adj[current]:
                if not visited[x]:
                    visited[x]=True
                    qu.append(x)
        return res