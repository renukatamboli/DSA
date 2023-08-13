#User function Template for python3

class Solution:
    def isSubsetSum(self, N, arr, target):
        dp = [[False for _ in range(target+1)] for _ in range(N)]
        
        # Initialize the first row of DP table
        for i in range(N):
            dp[i][0] = True
            
        if arr[0] <= target:
            dp[0][arr[0]] = True
        
        for i in range(1, N):
            for j in range(1, target+1):
                take = False
                if j >= arr[i]:
                    take = dp[i-1][j - arr[i]]
                notTake = dp[i-1][j]
                dp[i][j] = take or notTake
                
        return dp[N-1][target]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends
