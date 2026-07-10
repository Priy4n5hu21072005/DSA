from collections import deque
class sol:
    def Problem933(self,t):
        q = deque()
        q.append(t)  
        while q[0]<t-3000:
            q.popleft()
        return len(q)
