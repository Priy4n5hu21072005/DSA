from collections import deque
def topological_sort(adj):
    n=len(adj)
    indegree=[0]*n
    ans=[]
    que=deque()
    for i in range(n):
        for next_node in adj[i]:
            indegree[next_node]+=1
    for i in range(n):
        if indegree[i]==0:
            que.append(i)
    while que:
        top=que.popleft()
        ans.append(top)
        for next_node in adj[top]:
            indegree[next_node]-=1
            if indegree[next_node]==0:
                que.append(next_node)
    return ans