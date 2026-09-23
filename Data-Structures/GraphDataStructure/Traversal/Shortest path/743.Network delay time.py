import heapq
class Solution:
    def network_delay_time(n,k,times):
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        distance=[float("inf")]*(n+1)
        distance[k]=0
        pq=[(0,k)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>distance[u]:
                continue
            for v,w in graph[u]:
                new_distance=d+w
                if new_distance<distance[v]:
                    distance[v]=new_distance
                    heapq.heappush(pq,(new_distance,v))
        ans=max(distance[1:])
        if ans == float("inf"):
            return -1
        return ans
