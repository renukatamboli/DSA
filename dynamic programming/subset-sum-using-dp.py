#User function Template for python3

class Solution:
    def find(self,ind,target,arr,dp):
        if target == 0:
            return True
        if ind == 0:
            return target == arr[0]
        if dp[target][ind] != -1:
            return dp[target][ind]
        notTake = self.find(ind-1,target,arr,dp)
        take = False
        if target >= arr[ind]:
            take = self.find(ind-1,target-arr[ind],arr,dp)
        dp[target][ind] = take or notTake
        return dp[target][ind]
        
    def isSubsetSum(self, N, arr, target):
        dp = [[-1 for _ in range(0,N)]for _ in range(0,target+1)]
        return self.find(N-1,target,arr,dp)
        #for i in range(0,N):
        #    dp[i][0] = True
        #for i in range(1,N):
        #    for target in range(1,sum2+1):
        #        notTake = dp[i-1][target]
        #        take = False
        #        if arr[i] <= target:
        #            take = dp[i-1][target-arr[i]]
        #        dp[i][target] = take or notTake
        #return dp[N-1][sum2]        
        # code here 
        
        


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
