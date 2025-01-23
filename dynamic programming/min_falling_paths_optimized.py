class Solution:        
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        mini = 1e9
        for i in range(m-1,-1,-1):
            for j in range(0,n):
                if j == 0:
                    dp[i][j] = matrix[i][j]+min(dp[i+1][j],dp[i+1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j]+min(dp[i+1][j],dp[i+1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])
        for j in range(n):
            mini = min(mini,dp[0][j])
        return mini
