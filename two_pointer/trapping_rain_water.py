class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxleft = 0
        maxright = 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if maxleft < height[left]:
                    maxleft = height[left]
                else:
                    res += (maxleft - height[left])
                left += 1
            else:
                if maxright < height[right]:
                    maxright = height[right]
                else:
                    res += (maxright - height[right])
                right -= 1
        return res
