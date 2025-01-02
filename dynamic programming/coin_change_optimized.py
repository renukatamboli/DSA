class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [1e9 for _ in range(amount+1)] 
        dp[0] = 0 
        for i in range(0,len(coins)):
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j],1+dp[j-coins[i]])
        if dp[amount] != 1e9:
            return dp[amount]
        return -1
