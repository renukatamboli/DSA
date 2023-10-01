#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestChain(self, n, arr):
        arr.sort(key=len)
        dp = {}
        maxi = 0
        for word in arr:
            dp[word] = 1
            for ind in range(0,len(word)):
                pred = word[:ind]+word[ind+1:]
                if pred in dp and dp[pred]+1>dp[word]:
                    dp[word] = 1 + dp[pred]
                maxi = max(dp[word],maxi)
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
