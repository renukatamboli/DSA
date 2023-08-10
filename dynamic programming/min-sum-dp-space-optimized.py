import sys
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(0,n)] for j in range(0,m)] 
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    right = sys.maxsize
                    if i > 0:
                        right = grid[i][j]+ dp[i-1][j]
                    down = sys.maxsize
                    if j > 0:
                        down = grid[i][j]+ dp[i][j-1]
                    dp[i][j] = min(right,down)
        return dp[m-1][n-1] 
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
