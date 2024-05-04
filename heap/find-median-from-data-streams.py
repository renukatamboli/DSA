from collections import defaultdict
class MedianFinder:
            
    def __init__(self):
        self.arr = []
        self.l = 0
        
    def getIndex(self,low,high,num):
        mid = (low+high) // 2
        while low < high and low >= 0 and high <= self.l-2:
            mid = (low+high) // 2
            if self.arr[mid] >= num:
                high = mid
            else:
                low = mid+1
        return mid
                
                
            
        
    def insertSort(self,i):
        
        key = self.arr[self.l-1]

        j = self.l-2
        while j >= i and key < self.arr[j]:
            self.arr[j+1] = self.arr[j]
            j-=1
        self.arr[j+1] = key
        
                
        

    def addNum(self, num: int) -> None:
        
        self.arr.append(num)
        self.l += 1
        i = self.getIndex(0,self.l-2,num)
        self.insertSort(i)
        
        

    def findMedian(self) -> float:
        #print("arr",self.arr)
        if self.l == 0:
            return 0
        mid = self.l//2
        if self.l%2 == 0:
            return (self.arr[mid] + self.arr[mid-1]) / 2
        return self.arr[mid]
        
                
                
                
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
