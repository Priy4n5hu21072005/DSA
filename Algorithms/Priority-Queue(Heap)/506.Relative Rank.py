import heapq
class Solution:
    def RelativeRank(self,score:list[int])-> list[str]:
        n= len(score)
        heap =[]
        for i,s in enumerate(score):
            heap.append((-s,i))
        heapq.heapify(heap)
        ans = [""]*n
        rank = 1
        while heap:
            neg_score,idx = heapq.heappop(heap)
            if rank == 1:
                ans[idx]="Gold Medal"
            elif rank == 2:
                ans[idx]="Silver Medal"
            elif rank == 3:
                ans[idx]="Bronze Medal"
            else :
                ans[idx]=str(rank)
            rank +=1
        return ans   


score = [10,3,8,9,4]
obj = Solution()
print(obj.RelativeRank(score))
