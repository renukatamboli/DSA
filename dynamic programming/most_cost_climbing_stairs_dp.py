class Solution:
    def solve(self,cost,i,dp):
        if i >= len(cost):
            return 0
        if dp[i] != -1:
            return dp[i]
        dp[i] = cost[i] + min(self.solve(cost,i+1,dp),self.solve(cost,i+2,dp))
        return dp[i]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(0,len(cost))]
        return min(self.solve(cost,0,dp),self.solve(cost,1,dp))
