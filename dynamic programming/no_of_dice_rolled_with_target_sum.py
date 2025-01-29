class Solution:
    def solve(self,n,k,dp,i,target,mod):
        if i == n:
            if target <= k:
                return 1
            return 0
        
        if dp[i][target] != -1:
            return dp[i][target] % mod
        
        dp[i][target] = 0
        for t in range(1,k+1):
            if target - t > 0:
                dp[i][target] += (self.solve(n,k,dp,i+1,target-t,mod) % mod) 
        
        dp[i][target] = dp[i][target] % mod
        return dp[i][target]
            
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
        mod = 10**9+7
        return self.solve(n,k,dp,1,target,mod)
        
        
