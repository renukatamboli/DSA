class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 1
        intervals = sorted(intervals,key=lambda x:(x[1],x[0]))
        n = len(intervals)
        maxi = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] >= maxi:
                maxi = intervals[i][1]
                cnt+=1
        return n-cnt
