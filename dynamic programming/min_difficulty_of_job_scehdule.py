class Solution:
    def calculate(self,i,days,hardest_remaining, jobDifficulty,d, n, dp):
        hardest = 0
        best = 2 ** 31
        
        if (i,days) in dp:
            return dp[(i,days)]
        
        if d == days:
            return hardest_remaining[i]
        
        for j in range(i,n - (d - days)):
            hardest = max(hardest,jobDifficulty[j])
            best = min(best, hardest + self.calculate(j+1,days+1,hardest_remaining, jobDifficulty,d, n,dp))
        dp[(i,days)] = best
        return best
    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        hardest = 0
        n = len(jobDifficulty)
        hardest_remaining = [0 for _ in range(n)]
        
        
        if n < d:
            return -1 
        
        hardest_job = 0
        dp = {}
        
        for i in range(n-1, -1, -1):
            hardest_job = max(hardest_job,jobDifficulty[i])
            hardest_remaining[i] = hardest_job
        
            
        return self.calculate(0, 1, hardest_remaining, jobDifficulty,d, n,dp)
        
        
        
