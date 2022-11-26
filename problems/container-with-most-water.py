class Solution(object):
    def maxArea(self, height):
        max_area = 0
        length = len(height)
        low=0
        high = length-1
        for i in range(0,length):
            if(low > high):
                break
            max_area = max(max_area, min(height[low],height[high])*(length-1-i))
            if(height[low]<height[high]):
                low += 1
            else:
                high -= 1
        return max_area
                       
                         
        """
        :type height: List[int]
        :rtype: int
        """
        
