#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        ans = ""
        dp = [[-1 for i in range(0,n+1)] for j in range(0,m+1)]
        for j in range(0,n+1):
            dp[0][j] = 0
        for i in range(0,m+1):
            dp[i][0] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        t = n
        s = m
        while(s>0 and t>0):
            if X[s-1] == Y[t-1]:
                ans += X[s-1]
                s-=1
                t-=1
            elif dp[s-1][t] > dp[s][t-1]:
                ans += X[s-1]
                s-=1
            else:
                ans += Y[t-1]
                t-=1
        while(s>0):
            ans+=X[s-1]
            s-=1
        while(t>0):
            ans+=Y[t-1]
            t-=1
        return len(ans)
         #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends
