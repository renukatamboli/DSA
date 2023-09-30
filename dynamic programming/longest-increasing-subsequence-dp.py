#User function Template for python3

class Solution:
    def find(self,ind,prev_ind,a,n,dp):
        if ind == n:
            return 0
        if dp[ind][prev_ind+1] != -1:
            return dp[ind][prev_ind+1]
        l = self.find(ind+1,prev_ind,a,n,dp)
        if prev_ind == -1 or a[ind] > a[prev_ind]:
            l = max(l,1+self.find(ind+1,ind,a,n,dp))
        dp[ind][prev_ind+1] = l
        return l
            
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp =  [[-1 for _ in range(0,n)] for _ in range(0,n+1)]
        return self.find(0,-1,a,n,dp)
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
