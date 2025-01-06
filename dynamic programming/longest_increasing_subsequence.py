class Solution:
    def solve(self,i,nums,l,prev):
        if i == len(nums):
            return l
        take = 0
        if nums[i] > prev:
            take = self.solve(i+1,nums,l+1,nums[i])
        not_take = self.solve(i+1,nums,l,prev)
        return max(take,not_take)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve(0,nums,0,-1e8)
        
        
