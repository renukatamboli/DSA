class Solution:
    def findSubSets(self,nums,goal):
        if goal < 0:
            return 0
        l = 0
        r = 0
        cnt = 0
        n = len(nums)
        s = 0
        while r < n:
            s = s+ nums[r]
            while s > goal and l < n:
                s = s - nums[l]
                l += 1
            cnt = cnt + r-l+1
            r+=1
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.findSubSets(nums,goal) - self.findSubSets(nums,goal-1) 
