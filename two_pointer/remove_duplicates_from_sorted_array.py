class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        n = len(nums)
        while r < n:
            if nums[l] != nums[r]:
                l = l+1
                nums[l] = nums[r]
            r = r+1
        return l+1


        
