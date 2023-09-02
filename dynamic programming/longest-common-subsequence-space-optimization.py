#User function Template for python3

class Solution:
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        dp = [0 for i in range(0,y+1)]
        for i in range(1,x+1):
            temp = [0 for i in range(0,y+1)]
            for j in range(1,y+1):
                if s1[i-1] == s2[j-1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    temp[j] = max(dp[j],temp[j-1])
            dp = temp[:]
        return dp[y]


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
