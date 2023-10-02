#User function Template for python3

class Solution:
    def NumberofLIS(self, n, arr):
        dp  = [1 for _ in range(0,n)]
        cnt  = [1 for _ in range(0,n)]
        total = 0
        maxi = 0
        for i in range(1,n):
            for j in range(0,i):
                if arr[j] < arr[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]
                    elif dp[j]+1 == dp[i]:
                        cnt[i]+=cnt[j]
            maxi = max(maxi,dp[i])
        
        for t in range(0,n):
            if dp[t] == maxi:
                total+=cnt[t]
                
        return total
            
                    
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr= list(map(int, input().split()))
        ob = Solution()
        print(ob.NumberofLIS(n, arr))
# } Driver Code Ends
