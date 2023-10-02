#User function Template for python3

class Solution:
    
    def matrixMultiplication(self, N, arr):
        dp = [[0 for _ in range(0,N)] for _ in range(0,N)]
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                mini = 1e9
                for k in range(i,j):
                    steps = (arr[i-1]*arr[k]*arr[j]) + dp[i][k] + dp[k+1][j]
                    mini = min(mini,steps)
                dp[i][j] = mini
        return dp[1][N-1]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
