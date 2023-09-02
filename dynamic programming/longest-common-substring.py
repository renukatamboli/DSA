#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2, x, y):
        dp = [0 for i in range(0,y+1)]
        ans = 0
        for i in range(1,x+1):
            temp = [0 for i in range(0,y+1)]
            for j in range(1,y+1):
                if s1[i-1] == s2[j-1]:
                    temp[j] = 1 + dp[j-1]
                    ans = max(ans,temp[j])
                else:
                    temp[j] = 0
            dp = temp[:]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends
