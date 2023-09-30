#User function Template for python3

class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp = temp =  [0 for _ in range(0,n+1)] 
        for ind in range(n-1,-1,-1):
            for prev_ind in range(ind-1,-2,-1):
                l = dp[prev_ind+1]
                if prev_ind == -1 or a[ind] > a[prev_ind]:
                    l = max(l,1+dp[ind+1])
                temp[prev_ind+1] = l
            dp = temp[:]
                
        return dp[0]
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
