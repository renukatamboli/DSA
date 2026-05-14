class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l =0
        r = 0
        remove = 0
        maxi = float("-inf")
        count = 0
        found_zero = 0
        while r < len(nums):
            if nums[r] == 0:
                if l != r and nums[l] == 0:
                    count = r - l - 1
                l = r
                found_zero += 1
            elif nums[r] == 1:
                count += 1
            maxi = max(maxi, count)
            r+=1
        if found_zero == 0:
            maxi = maxi - 1
        return maxi
