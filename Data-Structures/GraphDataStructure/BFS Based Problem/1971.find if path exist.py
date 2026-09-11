from collections import deque
class Solution:
    def validPath(n:int,edges:list[list[int]],source:int,destination:int)->bool:
        adj_matrix=[[]for _ in range(n)]
        for u,v in edges:
            adj_matrix[u].append(v)
            adj_matrix[v].append(u)  
        visited=[False]*n  
        qu=deque([source])
        visited[source]=True
        while qu:
            current=qu.popleft()
            if current==destination:
                return True
            for x in adj_matrix[current]:
                if not visited[x]:
                    visited[x]=True
                    qu.append(x)
        return False