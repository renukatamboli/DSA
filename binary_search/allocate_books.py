class Solution:
    def calc(self,nums,mini):
        s = 0
        splits = 0
        for num in nums:
            if s + num > mini:
                s = num
                splits+=1
            else:
                s += num
        return splits

    def splitArray(self, nums: List[int], k: int) -> int:
        high = 0
        low = 0
        for num in nums:
            high+=num
            if num > low:
                low = num
        while low <= high:
            mid = (low+high) // 2
            split = self.calc(nums,mid)
            if split >= k:
                low = mid +1
            else:
                high = mid-1
        return low
