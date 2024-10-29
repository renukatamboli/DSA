class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        meet = []
        ans = 1
        l = len(start)
        for i in range(l):
            meet.append((start[i], end[i],i+1))
        meet = sorted(meet, key=lambda x: (x[1], x[2]))
        limit = meet[0][1]
        for i in range(1,l):
            if meet[i][0] > limit:
                ans+=1
                limit = meet[i][1]
        return ans
        # code here
