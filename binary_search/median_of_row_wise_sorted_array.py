import sys
class Solution:
    def upperbound(self,nums,m,target):
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countSmallEqual(self,mat,x):
        n = len(mat)
        m = len(mat[0])
        cnt = 0
        for i in range(n):
            cnt += self.upperbound(mat[i],m,x)
        return cnt

    def matrixMedian(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        low = sys.maxsize
        high = -sys.maxsize-1
        for i in range(n):
            low = min(grid[i][0], low)
            high = max(grid[i][m-1],high)
        req = (n*m) // 2
        while low <= high:
            mid = (low+high) // 2
            nums = self.countSmallEqual(grid,mid)
            if nums <= req:
                low = mid+1
            else:
                high = mid-1
        return low




        
