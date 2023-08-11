class Solution(object):

    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [-1 for i in range(0,n)]
        for j in range(0,n):
            dp[j] = triangle[n-1][j]
        for i in range(n-2,-1,-1):
            temp = [-1 for t in range(0,n)]
            for j in range(i,-1,-1):
                d = triangle[i][j] + dp[j]
                dg = triangle[i][j] + dp[j+1]
                temp[j] = min(d,dg)
            dp = temp[:]
        return dp[0]
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
