class Solution:        
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(0,2)] for _ in range(k+1)] for _ in range(n+1)] 
        for i in range(n-1,-1,-1):
            for j in range(k,0,-1):
                dp[i][j][1] = max(dp[i+1][j][0]-prices[i],dp[i+1][j][1])
                dp[i][j][0] = max(dp[i+1][j-1][1]+prices[i],dp[i+1][j][0])
        return dp[0][k][1]
        
