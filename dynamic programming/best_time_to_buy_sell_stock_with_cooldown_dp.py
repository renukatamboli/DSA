class Solution:
    def solve(self,prices,op,i,dp):
        if i >= len(prices):
            return 0
        if dp[i][op] != -1:
            return dp[i][op]
        take = 0
        not_take = 0
        if op == 0:
            take = -prices[i]+self.solve(prices,1,i+1,dp)
            not_take = self.solve(prices,0,i+1,dp)
        elif op == 1:
            take = prices[i] + self.solve(prices,2,i+1,dp)
            not_take = self.solve(prices,1,i+1,dp)
        else:
            take = self.solve(prices,0,i+1,dp)
        dp[i][op] = max(take,not_take)
        return dp[i][op]
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(0,3)] for _ in range(0,n+1)]
        return self.solve(prices,0,0,dp)
