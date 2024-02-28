class Solution:
        
    def DFS(self, i, nums, total, target,s,dp):
        if i == -1:
            if total == target:
                return 1
            else:
                return 0
        if dp[i][s+total] != 1e9:
            return dp[i][s+total]
        count=0
        count += self.DFS(i - 1, nums, total + nums[i], target,s,dp)
        count += self.DFS(i - 1, nums, total - nums[i], target,s,dp)
        dp[i][s+total] = count
        return count
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        s = sum(nums)
        total = 0
        dp = [[1e9 for _ in range(2*s+1)] for _ in range(l)]
        return self.DFS(l - 1, nums, total, target,s,dp)
