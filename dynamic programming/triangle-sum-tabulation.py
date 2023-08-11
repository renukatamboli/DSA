class Solution(object):

    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[-1 for i in range(0,j+1)] for j in range(0,n)]
        for j in range(0,n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                d = triangle[i][j] + dp[i+1][j]
                dg = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(d,dg)
        return dp[0][0]
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
