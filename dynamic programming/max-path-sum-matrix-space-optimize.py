#User function Template for python3

class Solution:
    def maximumPath(self, N, matrix):
        dp = [-1 for _ in range(0,N)]
        for j in range(0,N):
            dp[j] = matrix[0][j]
        for i in range(1,N):
            temp = [-1 for _ in range(0,N)]
            for j in range(0,N):
                top = matrix[i][j] + dp[j]
                ldg = matrix[i][j]
                rdg = matrix[i][j]
                if j > 0:
                    ldg += dp[j-1]
                if j < N-1:
                    rdg += dp[j+1]
                temp[j] = max(top,ldg,rdg)
            dp = temp[:]
        return max([dp[j] for j in range(0,N)])
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
