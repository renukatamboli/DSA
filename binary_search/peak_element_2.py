class Solution:
    def findMax(self,mat,mid):
        maxIndex = -1
        maxNum = -1
        for i in range(0,len(mat)):
            if mat[i][mid] > maxNum:
                maxNum = mat[i][mid]
                maxIndex = i
        return maxIndex 

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low = 0
        high = len(mat[0])-1
        while low <= high:
            mid = (low+high) // 2
            maxIndex = self.findMax(mat, mid)
            left = -1
            if mid - 1 >= 0:
                left = mat[maxIndex][mid-1]
            right = -1
            if mid+1 <= high:
                right = mat[maxIndex][mid+1]
            if mat[maxIndex][mid] > left and mat[maxIndex][mid] > right:
                return [maxIndex, mid]
            elif mat[maxIndex][mid] < left:
                high = mid-1
            else:
                low = mid+1
        return [-1,-1]

        
