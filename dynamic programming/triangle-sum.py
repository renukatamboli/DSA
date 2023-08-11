class Solution(object):
    def find(self,i,j,triangle,dp):
        if i == len(triangle)-1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        d = triangle[i][j] + self.find(i+1,j,triangle,dp)
        dg = triangle[i][j] + self.find(i+1,j+1,triangle,dp)
        dp[i][j] = min(d,dg)
        return dp[i][j]

    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[-1 for i in range(0,j+1)] for j in range(0,n)]
        return self.find(0,0,triangle,dp)
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
