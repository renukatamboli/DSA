import sys
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [-1 for t in range(0,n)] 
        for i in range(0,m):
            temp = [-1 for t in range(0,n)]
            for j in range(0,n):
                if i == 0 and j == 0:
                    temp[0] = grid[0][0]
                else:
                    right = sys.maxsize
                    if i > 0:
                        right = grid[i][j]+ dp[j]
                    down = sys.maxsize
                    if j > 0:
                        down = grid[i][j]+ temp[j-1]
                    temp[j] = min(right,down)
            dp = temp[:]
        return dp[n-1] 
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
