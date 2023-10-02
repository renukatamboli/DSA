#User function Template for python3

class Solution:
    def find(self,i,j,arr,dp):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = 1e9
        for k in range(i,j):
            steps = (arr[i-1]*arr[k]*arr[j]) + self.find(i,k,arr,dp) + self.find(k+1,j,arr,dp)
            mini = min(mini,steps)
        dp[i][j] = mini
        return dp[i][j]
    
    def matrixMultiplication(self, N, arr):
        dp = [[-1 for _ in range(0,N)] for _ in range(0,N)]
        return self.find(1,N-1,arr,dp)
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
