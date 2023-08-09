#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        dp = [[-1 for i in range(0,m)] for j in range(0,n)]
        for i in range(0,n):
            for j in range(0,m):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    left = 0
                    up = 0
                    if i > 0:
                        left = dp[i-1][j]
                    if j > 0:
                        up = dp[i][j-1]
                    dp[i][j] = left+up 
        return dp[n-1][m-1]
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
