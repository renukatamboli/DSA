class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums)-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i+1
                hi = len(nums)-1
                s = -nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == s:
                        res.append([nums[i],nums[lo],nums[hi]])

                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo+=1

                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi-=1

                        lo+=1
                        hi-=1
                    elif nums[lo]+ nums[hi] < s:
                        lo+=1
                    else:
                        hi-=1
        return res

        
