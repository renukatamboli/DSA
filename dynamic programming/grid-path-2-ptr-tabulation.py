#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        dp = [-1 for t in range(0,m)]
        for i in range(0,n):
            temp = [-1 for t in range(0,m)]
            for j in range(0,m):
                if i==0 and j == 0:
                    temp[j] = 1
                else:
                    left = 0
                    up = 0
                    if i > 0:
                        left = dp[j]
                    if j > 0:
                        up = temp[j-1]
                    temp[j] = left+up
            dp = temp[:]
        return dp[m-1]
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
