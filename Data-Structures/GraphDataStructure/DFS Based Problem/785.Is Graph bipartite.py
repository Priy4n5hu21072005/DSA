class Solution:
    def isGraphBipartite(self,graph):
        n=len(graph)
        color=[0]*n
        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor]==0:
                    color[neighbor]=3-color[node]
                    if not dfs(neighbor):
                        return False
                elif color[node]==color[neighbor]:
                    return False
            return True
        for i in range(n):
            if color[i]==0:
                color[i]=1
                if not dfs(i):
                    return False    
        return True