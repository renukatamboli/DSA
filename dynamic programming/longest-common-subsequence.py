#User function Template for python3

class Solution:
    
    def find(self,x,y,s1,s2,dp):
        if x < 0 or y < 0:
            return 0
        if dp[x][y] != -1:
            return dp[x][y]
        if s1[x] == s2[y]:
            dp[x][y] = 1 + self.find(x-1,y-1,s1,s2,dp)
            return dp[x][y]
        dp[x][y]= max(self.find(x-1,y,s1,s2,dp),self.find(x,y-1,s1,s2,dp))
        return dp[x][y]
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        dp = [[-1 for i in range(0,y+1)] for j in range(0,x+1)]
        return self.find(x-1,y-1,s1,s2,dp)
        
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
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
