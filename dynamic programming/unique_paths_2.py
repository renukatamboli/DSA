class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    flag = 0
                    if i>0 and dp[i-1][j] != 0:
                        flag += 1
                    if j>0 and dp[i][j-1] !=0:
                        flag+=1
                    
                    if flag == 0 and not (i==0 and j==0):
                        dp[i][j] = 0
                        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
        
