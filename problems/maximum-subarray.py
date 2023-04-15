import math
class Solution(object):
    def maxSubArray(self, nums):
        maxSum = - math.pow(10,5)
        curr_sum = 0
        for i in range(0, len(nums)):
            curr_sum = curr_sum + nums[i]
            maxSum = max(maxSum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return maxSum
