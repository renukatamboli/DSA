#User function Template for python3

class Solution:
    def find(self,ind,buy,K,N,arr,dp):
        if ind == N or K==0:
            return 0
        if dp[ind][buy][K] != -1:
            return dp[ind][buy][K]
        if buy:
            dp[ind][buy][K] = max((-arr[ind]+self.find(ind+1,0,K,N,arr,dp)),self.find(ind+1,1,K,N,arr,dp))
        else:
            dp[ind][buy][K] = max((arr[ind]+self.find(ind+1,1,K-1,N,arr,dp)),self.find(ind+1,0,K,N,arr,dp))
        return dp[ind][buy][K]
        
    def maxProfit(self, K, N, A):
        dp = [[[-1 for _ in range(0,K+1)] for _ in range(0,2)]for _ in range(0,N+1)]
        return self.find(0,1,K,N,A,dp)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends
