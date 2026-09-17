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
        for i in range(len(adj)):
            if not visited[i]:
                self.dfsRect(adj,visited,i,res) 
        return res