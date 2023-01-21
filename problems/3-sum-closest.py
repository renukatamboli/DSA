class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = 1000000
        min_sum = 0
        for i in range(0,len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            lo = i+1
            hi = len(nums)-1
            while(lo<hi):
                if(abs((nums[lo]+nums[hi]+nums[i])-target)<min_diff):
                    min_sum = nums[lo]+nums[hi]+nums[i]
                    min_diff = abs(target -(nums[lo]+nums[hi]+nums[i]))
                elif(nums[lo]+nums[hi]+nums[i]<target):
                    lo+=1
                else:
                    hi-=1
                #print("min_diff",min_diff)
        return min_sum
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
Console
