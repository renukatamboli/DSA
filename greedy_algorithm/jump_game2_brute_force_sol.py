class Solution:
    def getJump(self,i,nums,mini,jumps):
        if i >= len(nums)-1:
            return jumps
        for ind in range(1,nums[i]+1):
            mini[0] = min(mini[0], self.getJump(ind+i,nums,mini,jumps+1))
        return mini[0]

    def jump(self, nums: List[int]) -> int:
        mini = [1000000000000]
        return self.getJump(0,nums,mini,0)
