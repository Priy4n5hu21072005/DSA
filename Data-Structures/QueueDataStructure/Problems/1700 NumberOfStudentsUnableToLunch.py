# Brute Force
from collections import deque
class sol1:
    def Problem1700(self,sand,stu):
        q=deque(stu)
        i=0  
        fail =0
        while q and fail < len(q):
            if q[0]==sand[i]:
                q.popleft()
                i+=1
                fail=0
            else:
                q.append(q.popleft)
                fail+=1
        return len(q)
    
    #Time complexity = O(n^2)


    #Optimal Solution
class sol2:
    def Pro1700(self,stu,sand):
        count =[0,0]
        for s in stu:
            count[s]+=1
        for s in sand:
            if count[s]==0:
                break
            count[s]-=1
        return count[1]+count[0]