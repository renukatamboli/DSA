class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j != n-1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif i != m-1 and j == n-1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif i != m-1 and j != n-1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]
