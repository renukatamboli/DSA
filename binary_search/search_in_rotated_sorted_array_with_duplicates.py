class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        n = len(nums)
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                 return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[mid] >= nums[low]:
                if nums[mid] >= target and nums[low] <= target:
                    high = mid-1
                else:
                    low = mid + 1
            if nums[mid] <= nums[high]:
                if nums[mid] <= target and nums[high] >= target:
                    low = mid+1
                else:
                    high = mid-1
        return False

        
