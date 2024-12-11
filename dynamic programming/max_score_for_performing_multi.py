class Solution:   
             
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        
        memo = {}
        
        def calculate(i,left):
            if i == m:
                return 0
            
            if (i,left) in memo:
                return memo[(i,left)]
            
            right = n - 1 - (i-left)
            
            pick_left = multipliers[i]*nums[left] + calculate(i+1,left+1)
            pick_right = multipliers[i]*nums[right] + calculate(i+1,left)
            
            memo[(i,left)] = max(pick_left,pick_right)
            return memo[(i,left)]
            
        return calculate(0,0)
