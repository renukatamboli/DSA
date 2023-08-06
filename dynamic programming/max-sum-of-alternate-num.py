#User function Template for python3

class Solution:  
    def find(self,index,a,dp):
        if index == 0:
            return a[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        
        pick = a[index] + self.find(index-2,a,dp)
        not_pick = self.find(index-1,a,dp)
        
        dp[index] = max(pick,not_pick)
        return dp[index]
            
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        dp = [-1 for i in range(0,n)]
        return self.find(n-1,a,dp)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends
