class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.tempArr = nums[0:k]
        l = len(self.tempArr)
        for i in range(l//2 -1 , -1, -1):
            self.heapify(l,i)
            
        for i in range(self.k,len(self.nums)):
            if self.nums[i] >= self.tempArr[0]:
                self.tempArr[0] = self.nums[i]
                self.heapify(l,0)
        
    def heapify(self,size,index):
        left = 2*index+1
        right = 2*index+2
        
        smallest = index
        if left < size and self.tempArr[left] < self.tempArr[smallest]:
            smallest = left
        if right < size and self.tempArr[right] < self.tempArr[smallest]:
            smallest = right
        if smallest != index:
            self.tempArr[smallest], self.tempArr[index] = self.tempArr[index], self.tempArr[smallest]
            self.heapify(size,smallest)
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        
        l = len(self.tempArr)
        if len(self.tempArr) == self.k and self.nums[-1] >= self.tempArr[0]:
            self.tempArr[0] = self.nums[-1]
            self.heapify(l,0)
        else:
            if len(self.tempArr) < self.k:
                self.tempArr.append(val)
                l = len(self.tempArr)
                self.heapify(l,0)
        return self.tempArr[0]
        
        
    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
