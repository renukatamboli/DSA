class Solution:           
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[i][mid] > target:
                    high = mid - 1
                elif matrix[i][mid] < target:
                    low = mid+1
                else:
                    return True
        return False
