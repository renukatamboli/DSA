#User function Template for python3
import sys
class Solution:
    def find(self,ind,w,wt,val,dp):
        if ind == 0:
            if wt[ind] <= w:
                return val[ind]
            else:
                return 0
        if dp[ind][w] != -1:
            return dp[ind][w]
        notTake = self.find(ind-1,w,wt,val,dp)
        take = 0
        if wt[ind] <= w:
            take = val[ind] + self.find(ind-1,w - wt[ind],wt,val,dp)
        dp[ind][w] = max(take,notTake)
        return dp[ind][w]
                
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[-1 for _ in range(0,W+1)] for _ in range(0,n)]
        # for i in range(n):
        #     if wt[i] <= w:
        #         dp[i][0] = val[i]
        #     else:
        #         dp[i][0] = 0
                
        # for i in range(1,n):
        #     for j 
        return self.find(n-1,W,wt,val,dp)
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
