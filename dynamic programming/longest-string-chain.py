#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def checkPossible(self,s1,s2):
        l1 = 0
        l2 = 0
        if len(s1) != len(s2) + 1:
            return False
        while(l1 < len(s1)):
            if l2 < len(s2) and s1[l1] == s2[l2]:
                l1+=1
                l2+=1
            else:
                l1+=1
        if l1 == len(s1) and l2 == len(s2):
            return True
        return False
            
    def longestChain(self, n, arr):
        arr.sort(key=len)
        dp = [1 for _ in range(0,n+1)]
        maxi = 0
        for ind in range(1,n):
            for prev in range(0,ind):
                if 1 + dp[prev] > dp[ind] and self.checkPossible(arr[ind],arr[prev]):
                    dp[ind] = 1 + dp[prev]
                if dp[ind] > maxi:
                    maxi = dp[ind]
        return maxi
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        words = input().split()
        ob = Solution()
        res = ob.longestChain(N, words)
        print(res)
# } Driver Code Ends
