class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                l = j+1
                r = n-1
                remain = target - (nums[i]+nums[j])
                while l<r:
                    if nums[l]+nums[r] == remain:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l+=1
                        r-=1
                    elif nums[l]+nums[r] > remain:
                        r-=1
                    else:
                        l+=1
        return ans

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
