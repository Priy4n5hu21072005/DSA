class Solution:
    def dfsRect(self,adj,visited,s,res):
        visited[s]=True
        res.append(s)
        for i in adj[s]:
            if not visited[i]:
                self.dfsRect(adj,visited,i,res)  
    def dfs(self,adj):
        visited=[False]*len(adj)
        res=[]
        self.dfsRect(adj,visited,0,res)
        return res