from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph=[[]for _ in range(n+1)]
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color=[0]*(n+1)
        for i in range(1,n+1):
            if color[i]!=0:
                continue
            que=deque()
            color[i]=1
            que.append(i)  
            while que:
                node=que.popleft()
                for neighbor in graph[node]:
                    if color[neighbor]==0:
                        color[neighbor]=3-color[node]
                        que.append(neighbor)
                    elif color[node]==color[neighbor]:
                        return False
        return True