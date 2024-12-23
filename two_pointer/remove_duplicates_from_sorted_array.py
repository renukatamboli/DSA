class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        t = 0
        n = len(nums)
        while l < n and r < n and t <n:
            if nums[t] != nums[r]:
                nums[l+1] = nums[r]
                l = l+1
                t = r
            r = r+1
        return l+1

        
