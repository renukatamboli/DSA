class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = {}
        for i in range(0,len(nums)):
            if nums[i] in hashSet:
                if i - hashSet[nums[i]] <= k:
                    return True
                else:
                    hashSet[nums[i]] = i
            else:
                hashSet[nums[i]] = i 
        return False

        
