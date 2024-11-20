class Solution:
    def mergeSort(self,nums):
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left_list = self.mergeSort(nums[0:pivot])
        right_list = self.mergeSort(nums[pivot:])
        
        return self.merge(left_list,right_list)
    
    def merge(self,left,right):
        l = 0
        r = 0
        
        ret = []
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ret.append(left[l])
                l+=1
            else:
                ret.append(right[r])
                r+=1
        
        while l < len(left):
            ret.append(left[l])
            l+=1
        
        while r < len(right):
            ret.append(right[r])
            r+=1
        
        return ret
        
        
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        
