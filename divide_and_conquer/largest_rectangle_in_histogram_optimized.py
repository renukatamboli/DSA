class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                width = heights[stack.pop()]
                height = i - stack[-1] - 1
                area = max(area,width*height)
            stack.append(i)
        
        while stack[-1] != -1:
                width = heights[stack.pop()]
                height = len(heights) - stack[-1] - 1
                area = max(area,width*height)            
        
        return area
