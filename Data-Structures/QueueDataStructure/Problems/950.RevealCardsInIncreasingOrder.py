from collections import deque
class sol:
    def Problme950(self,deck):
        deck.sort()
        op=[0]*len(deck)
        q=deque(range(len(deck)))
        for i in deck:
            idx = q.popleft()
            op[idx]=i
            if q:
                q.append(q.popleft())
        return op   