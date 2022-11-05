class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            if(target-nums[i] in nums):
                index = len(nums) - nums[::-1].index(target-nums[i]) - 1
                if(i!=index):
                    return (i, index)




#https://leetcode.com/problems/two-sum/submissions/