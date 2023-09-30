#User function Template for python3

class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp =  [1 for _ in range(0,n+1)] 
        maxi = 1
        for ind in range(0,n):
            for prev in range(0,ind):
                if a[ind] > a[prev]:
                    dp[ind] = max(dp[ind],1+dp[prev])
            maxi = max(maxi,dp[ind]) 
        return maxi
        # code here
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends
