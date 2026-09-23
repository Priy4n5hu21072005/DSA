from collections import heapq
def dijkstra(adj,src):
    V=len(adj)
    pq=[]

    distance=[float("-inf")]*V
    distance[src]=0
    heapq.heappush(pq,(0,src))
    while pq:
        d,u=heapq.heappop(pq)
        if d>distance[u]:
            continue
        for v,w in adj[u]:
            if distance[u]+w>distance[v]:
                distance[v]=distance[u]+w
                heapq.heappush(pq,(distance[v],v))
    return distance

