#User function Template for python3

class Solution:
    def find(self,n,m,dp):
        if n==0 and m == 0:
            return 1
        if n < 0 or m < 0:
            return 0
        if dp[n][m] != -1:
            return dp[n][m] 
        left = self.find(n,m-1,dp)
        up = self.find(n-1,m,dp)
        dp[n][m] = left+up
        return dp[n][m]
        
    def numberOfPaths (self, n, m):
        dp = [[-1 for i in range(0,m)] for j in range(0,n)]
        return self.find(n-1,m-1,dp)
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends
