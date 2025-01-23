class Solution:
    def solve(self,m,n,matrix,dp,i,j):
        if i == n-1 and j >= 0 and j < m:
            return matrix[i][j]
        elif i >= 0 and j >= 0 and i < m and j < n:
            if dp[i][j] != 1e9:
                return dp[i][j]
            dp[i][j] = matrix[i][j] + min(self.solve(m,n,matrix,dp,i+1,j-1), self.solve(m,n,matrix,dp,i+1,j) , self.solve(m,n,matrix,dp,i+1,j+1))
            return dp[i][j]
        else:
            return 1e9
        
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[1e9 for _ in range(n)] for _ in range(m)]
        mini = 1e9
        for j in range(n):
            mini = min(mini,self.solve(m,n,matrix,dp,0,j))
        return mini
