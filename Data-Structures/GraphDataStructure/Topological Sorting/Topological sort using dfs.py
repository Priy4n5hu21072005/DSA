def findtoposort(node,visit,adj,stack):
    visit[node]=1
    for i in adj[node]:
        if visit[i]==0:
            findtoposort(i,visit,adj,stack)
    stack.append(node)

def toposort(adj):
    n=len(adj)
    stack=[]
    visit=[0]*n
    for i in range(n):
        if visit[i]==0:
            findtoposort(i,visit,adj,stack)
    topo=[]
    while stack:
        topo.append(stack.pop())
    return topo