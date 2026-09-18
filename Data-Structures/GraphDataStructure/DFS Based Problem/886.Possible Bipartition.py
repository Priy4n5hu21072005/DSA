class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph=[[] for _ in range(n+1)]
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)  
        color=[0]*(n+1)
        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor]==0:
                    color[neighbor]=3-color[node]
                    if not dfs(neighbor):
                        return False
                elif color[node]==color[neighbor]:
                    return False
            return True
        for i in range(1,n+1):
            if color[i]==0:
                color[i]=1
                if not dfs(i):
                    return False
        return True