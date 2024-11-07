class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        n = len(nums)
        longStreak = 0
        for i in range(0,n):
            numSet.add(nums[i])
            
        for i in range(0,n):
            cur = nums[i]
            streak = 1
            if cur-1 in numSet:
                continue
            while cur+1 in numSet:
                cur = cur+1
                streak+=1
            longStreak = max(streak,longStreak)
        return longStreak 
