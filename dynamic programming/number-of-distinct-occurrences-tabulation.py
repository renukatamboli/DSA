# Your task is to complete this function
# Finction should return Integer
class Solution:
            
    def sequenceCount(self,arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        dp = [[0 for _ in range(0,n+1)] for _ in range(0,m+1)]
        for t in range(0,m+1):
            dp[t][0] = 1  
        for i in range(1,m+1):
            for j in range(1,n+1):
                if arr1[i-1] == arr2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                dp[i][j] = int(dp[i][j] % (1e9+7))
        return dp[m][n]
        # Code here


#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends
