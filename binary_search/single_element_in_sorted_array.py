class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if high == 0:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[high] != nums[high-1]:
            return nums[high]
        high = high-1
        low = low+1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                low = mid+1
            else:
                high = mid-1
        return -1 

        
        
