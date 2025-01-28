class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        sets = []
        if len(nums) == 0:
            sets.append([lower,upper])
            return sets
        if nums[0] == lower and nums[0] == upper:
            return sets
        if nums[0] > lower:
            sets.append([lower,nums[0]-1])
        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                sets.append([nums[i]+1,nums[i+1]-1])
        if nums[len(nums)-1] == upper:
            return sets
        if nums[len(nums)-1]+1 <= upper:
            sets.append([nums[len(nums)-1]+1,upper])
        return sets   
