class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [[1e9 for _ in range(amount+1)] for _ in range(len(coins))]
        for k in range(amount+1):
            if k % coins[0] == 0:
                dp[0][k] = (k // coins[0])
        for i in range(1,len(coins)):
            for j in range(0,amount+1):
                if coins[i]<= j:
                    dp[i][j] = min(dp[i-1][j],1+dp[i][j-coins[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[len(coins)-1][amount] != 1e9:
            return dp[len(coins)-1][amount]
        return -1
