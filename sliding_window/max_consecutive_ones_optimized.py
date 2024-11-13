class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        z = 0
        n = len(nums)
        maxlen = 0
        while r < n:
            if nums[r] == 0:
                z+=1
            if z > k:
                if nums[l] == 0:
                    z-=1
                l += 1
            if z <= k:
                maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen
            
        
