class Solution:
    def solve(self,dp,prices,fee,i, buy):
        if i >= len(prices):
            return 0
        if dp[i][buy] != -1:
            return dp[i][buy]
        take = 0
        not_take = 0
        if buy:
            take = self.solve(dp, prices, fee, i + 1, 0) - prices[i]
            not_take = self.solve(dp, prices, fee, i + 1, 1)
        else:
            take = self.solve(dp, prices, fee, i + 1, 1) + prices[i] - fee
            not_take = self.solve(dp, prices, fee, i + 1, 0)
        dp[i][buy] = max(take, not_take)
        return dp[i][buy]
            
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[-1 for _ in range(0,2)] for _ in range(0,len(prices))]
        return self.solve(dp,prices,fee,0,1)
        
