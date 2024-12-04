class Solution:
    def calculate(self,heights,start,end):
        if start > end:
            return 0
        min_index = start
        for i in range(start,end+1):
            if heights[min_index] > heights[i]:
                min_index = i
        return max(heights[min_index]*(end-start+1),self.calculate(heights,start,min_index-1), self.calculate(heights,min_index+1,end))
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calculate(heights,0,len(heights)-1)
