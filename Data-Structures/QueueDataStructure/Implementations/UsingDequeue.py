from collections import deque
q=deque()
q.append('a')
q.append('b')
q.append('c')
print("Intial Queue after inserting element",q)
print("After remove each and every element")
while q :
    print(q.popleft())