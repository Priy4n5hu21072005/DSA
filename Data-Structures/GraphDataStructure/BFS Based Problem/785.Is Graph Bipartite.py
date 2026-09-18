from collections import deque
class Solution:
    def IsGraphBipartite(self,graph):
        n=len(graph)
        color=[0]*n
        for i in range(n):
            if color[i]!=0:
                continue
            qu=deque()
            color[i]=1
            qu.append(i)  
            while qu:
                node=qu.popleft()
                for neighbor in graph[node]:
                    if color[neighbor]==0:
                        color[neighbor]=3-color[node]
                        qu.append(neighbor)
                    elif color[node]==color[neighbor]:
                        return False
        return True