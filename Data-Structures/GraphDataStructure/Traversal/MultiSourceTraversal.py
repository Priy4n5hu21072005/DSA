from collections import deque
class Solution:
    def multi_source_vertex(vertex,edges,sources):
        graph=[[]for _ in range(vertex)]
        for u,v in edges:
            graph[u].append(v)  
            graph[v].append(u)  
        qu=deque()
        distance=[-1]*vertex
        for source in source:
            qu.append(source)
            distance[source]=0
        while qu:
            current_value=qu.popleft()
            for neighbour in graph[current_value]:
                if distance[neighbour]==-1:
                    distance[neighbour]=distance[current_value]+1
                    qu.append(neighbour)
        return distance