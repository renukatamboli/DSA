#https://leetcode.com/problems/find-median-from-data-stream/description/?envType=problem-list-v2&envId=heap-priority-queue
from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.l = []
        self.h = []
        
    def addNum(self, num: int) -> None:
        heappush(self.l, -num)
        heappush(self.h, -heappop(self.l))
        
        if len(self.l) < len(self.h):
            heappush(self.l, -heappop(self.h))

    def findMedian(self) -> float:
        if len(self.l) > len(self.h):
            return -self.l[0]
        return (-self.l[0] + self.h[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
