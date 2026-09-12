from collections import deque
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=set()
        
        #new provinces find karna 
        provinces=0
        for city in range(n):
            if city not in visited:
                #provinces ko update kar
                provinces+=1
                que=deque()
                que.append(city)
                visited.add(city)
                #BFS
                while que:
                    current=que.popleft()
                    for x in range(n):
                         #connected privinces ki citites visit karna 
                        if isConnected[current][x]==1:
                            if x not in visited:
                                visited.add(x)
                                que.append(x)
        return provinces
       

        
       

       