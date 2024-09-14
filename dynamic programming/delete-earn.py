from collections import defaultdict
class Solution:    
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_num = 0
        for num in nums:
            points[num] += num
            max_num = max(max_num,num)
        
        dp = [-1 for _ in range(max_num+1)]
        dp[0] = 0
        dp[1] = points[1]
        
        for i in range(2,max_num+1):
            dp[i] = max(dp[i-1],dp[i-2]+points[i])
            
        return dp[max_num]
        
        
        
        
