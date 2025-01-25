#https://leetcode.com/explore/learn/card/dynamic-programming/647/more-practice-problems/4074/

class Solution:
    def solve(self,costs,dp,i,prevColor):
        if i == len(costs):
            return 0
        if dp[i][prevColor] != -1:
            return dp[i][prevColor]
        mini = 1e9
        for j in range(len(costs[0])):
            if j != prevColor:
                dp[i][prevColor] = costs[i][prevColor] + self.solve(costs,dp,i+1,j)
                mini = min(dp[i][prevColor], mini)
        if mini != 1e9:
            dp[i][prevColor] = mini
        return dp[i][prevColor]
                
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        mini = 1e9
        for j in range(len(costs[0])):
            dp[0][j] = self.solve(costs,dp,0,j)
            mini = min(mini,dp[0][j])
        return mini
        
