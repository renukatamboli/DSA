#User function Template for python3

class Solution:
    def isSubsetSum(self, N, arr, target):
        dp = [False for _ in range(target+1)]
        
        dp[0] = True
            
        if arr[0] <= target:
            dp[arr[0]] = True
        
        for i in range(1, N):
            temp = [False for _ in range(target+1)]
            for j in range(1, target+1):
                take = False
                if j >= arr[i]:
                    take = dp[j - arr[i]]
                notTake = dp[j]
                temp[j] = take or notTake
            dp = temp[:]    
        return dp[target]
        
        


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
