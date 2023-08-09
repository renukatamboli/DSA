import sys
class Solution(object):
    def f(self,i,j,grid,dp):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return sys.maxsize
        if dp[i][j] != -1:
            return dp[i][j]
        up = grid[i][j] + self.f(i-1,j,grid,dp)
        left =  grid[i][j] + self.f(i,j-1,grid,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(0,n)] for j in range(0,m)]
        return self.f(m-1,n-1,grid,dp) 
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
