class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = low
        high = len(nums)-1

        while(mid<=high):
            if(nums[mid]==0):
                self.swap(nums,low,mid)
                low+=1
                mid+=1
                continue
            if(nums[mid]==2):
                self.swap(nums,mid,high)
                high-=1
                continue
            mid+=1  
        return nums

    def swap(self,nums,index1,index2):
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp
