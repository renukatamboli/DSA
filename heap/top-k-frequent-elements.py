from collections import defaultdict
class Solution:
    def heapify(self,nums,l,index,count):
        left = 2*index+1
        right = 2*index+2
        
        largest = index
        
        if left < l and count[nums[left]] > count[nums[largest]]:
            largest = left
        if right < l and count[nums[right]] > count[nums[largest]]:
            largest = right
        if largest != index:
            nums[largest],nums[index] = nums[index],nums[largest] 
            self.heapify(nums,l,largest,count)
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        l = len(set(nums))
        nums = list(set(nums))
        for i in range(l // 2 - 1, -1, -1):
            self.heapify(nums, l, i,count)
        for t in range(0,k):
            nums[0],nums[l-1] = nums[l-1],nums[0]
            ans.append(nums[l-1])
            l=l-1
            self.heapify(nums,l,0,count)
        return ans
        
        
