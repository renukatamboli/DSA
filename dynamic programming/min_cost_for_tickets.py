class Solution:
    def solve(self,days,costs,curday,isTravelNeeded,dp):
        if curday > days[len(days)-1]:
            return 0
        if dp[curday] != -1:
            return dp[curday]
        
        if curday not in isTravelNeeded:
            return self.solve(days,costs,curday+1,isTravelNeeded,dp)
        
        one = costs[0] + self.solve(days,costs,curday+1,isTravelNeeded,dp)
        seven = costs[1] + self.solve(days,costs,curday+7,isTravelNeeded,dp)
        thirty = costs[2] + self.solve(days,costs,curday+30,isTravelNeeded,dp)
        
        dp[curday] = min(one,seven,thirty)
        
        return dp[curday]
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        isTravelNeeded = set()
        dp = [-1 for _ in range(days[len(days)-1]+1)]
        for day in days:
            isTravelNeeded.add(day)
        return self.solve(days,costs,0,isTravelNeeded,dp)
        
