class Solution:   
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(1,len(coins)):
            for j in range(0,amount+1):
                if coins[i] <= j:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)-1][amount]
