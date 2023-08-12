#https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

#User function Template for python3

class Solution:
    def find(self,i,j,matrix,dp,n):
        if j<0 or j>=n:
            return -1e9
        if i==0:
            return matrix[0][j]
        if dp[i][j] != -1:
            return dp[i][j]
        top = matrix[i][j] + self.find(i-1,j,matrix,dp,n)
        ldg = matrix[i][j] + self.find(i-1,j-1,matrix,dp,n)
        rdg = matrix[i][j] + self.find(i-1,j+1,matrix,dp,n)
        dp[i][j] = max(top,ldg,rdg)
        return dp[i][j]
        
    def maximumPath(self, N, Matrix):
        dp = [[-1 for _ in range(0,N)] for _ in range(0,N)]
        for t in range(0,N):
            dp[N-1][t] = self.find(N-1,t,Matrix,dp,N)
        return max([dp[N-1][j] for j in range(0,N)])
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends
