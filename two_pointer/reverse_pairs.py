class Solution:
    def merge(self, low,mid, high, nums):
        i = low
        j = mid+1
        cnt = 0
        for i in range(low, mid+1):
            while j <= high and nums[i] > 2*nums[j]:
                j+=1
            cnt += (j - (mid+1))
        temp = []
        left = low
        right = mid+1
        while left < mid+1 and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1

        while left < mid+1:
            temp.append(nums[left])
            left+=1
        
        while right <= high:
            temp.append(nums[right])
            right+=1

        for k in range(low, high+1):
            nums[k] = temp[k-low]

        return cnt


    def mergeSort(self,low, high,nums):
        if low >= high:
            return 0    
        mid = (low+high) // 2
        inv = self.mergeSort(low,mid,nums)
        inv += self.mergeSort(mid+1,high,nums)
        inv += self.merge(low,mid,high,nums)
        return inv

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(0,len(nums)-1,nums)
        
