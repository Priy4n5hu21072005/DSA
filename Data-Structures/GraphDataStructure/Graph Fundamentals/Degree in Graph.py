class Solution:
    def FindInOutDegree(adj):
        n=len(adj)
        inDegree=[0]*n
        outDegree=[0]*n
        for i in range(n):
            outDegree[i]=len(adj[i])
            for v in adj[i]:
                inDegree[v]+=1
        result=[[inDegree[i],outDegree[i]]for i in range(n)]
        return result