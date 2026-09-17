class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans=[]
        path=[0]
        def dfs(node):
            if node == len(graph)-1:
                ans.append(path.copy())
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()
        dfs(0)
        return ans