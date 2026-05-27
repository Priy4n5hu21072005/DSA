# Problem 56 : Merge Intervals
class solution:
    def MergeIntervals(self,intervals):
        if not intervals:
            return []
        intervals.sort()
        res=[intervals[0]]
        for s , e in intervals:
            Lend=res[-1][1]
            if s <= Lend:
                res[-1][1]=max(Lend,e)
            else:
                res.append([s,e])
        return res

intervals=[[1,3],[2,6],[8,10],[15,18]]
print(solution().MergeIntervals(intervals))