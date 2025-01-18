class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum = nums[0]
        max_sum = nums[0]
        total = 0
        cur_min = 0
        cur_max = 0
        for num in nums:
            cur_min = min(cur_min+num,num)
            min_sum = min(min_sum,cur_min)

            cur_max = max(cur_max+num,num)
            max_sum = max(max_sum,cur_max)

            total += num
        if total == min_sum:
            return max_sum
        return max(max_sum, total - min_sum)
        
