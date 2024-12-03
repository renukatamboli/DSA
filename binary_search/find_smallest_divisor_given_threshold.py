import math
class Solution:
    def check(self,d,nums,t):
        ans = 0
        for num in nums:
            ans +=  math.ceil(num / d)
        return ans

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0
        while low <= high:
            mid = (low+high) // 2
            if self.check(mid,nums,threshold) <= threshold:
                high = mid-1
            else:
                low = mid+1
        return low
