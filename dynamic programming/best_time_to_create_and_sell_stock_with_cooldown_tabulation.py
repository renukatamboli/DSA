class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(0,3)] for _ in range(0,n+1)]
        for i in range(n-1,-1,-1):
            dp[i][0] = max(dp[i+1][1] - prices[i], dp[i+1][0])
            dp[i][1] = max(prices[i]+dp[i+1][2],dp[i+1][1])
            dp[i][2] = dp[i+1][0]
        return dp[0][0]
