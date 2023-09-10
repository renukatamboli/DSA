# Your task is to complete this function
# Finction should return Integer
class Solution:
    def find(self,i,j,arr1,arr2,dp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if arr1[i] == arr2[j]:
            dp[i][j] = self.find(i-1,j-1,arr1,arr2,dp) + self.find(i-1,j,arr1,arr2,dp)
        else:
            dp[i][j] = self.find(i-1,j,arr1,arr2,dp)
        return int(dp[i][j] % (1e9+7))
            
    def sequenceCount(self,arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        dp = [[-1 for i in range(0,n+1)] for j in range(0,m+1)]
        return self.find(m-1,n-1,arr1,arr2,dp)
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
