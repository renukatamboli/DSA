class Solution:
    def upperbound(self,mat,i,n, num):
        low = 0
        high = n-1
        index = -1
        while low <= high:
            mid = (low+high) // 2
            if mat[i][mid] == num:
                index = mid
                low = mid+1
            else:
                high = mid-1
        return index+1
        
    def rowWithMax1s(self, arr):
        count_ones = 0
        n = len(arr[0])
        m = len(arr)
        ans = -1
        max_ones = 0
        for i in range(m):
            cnt_zeroes = self.upperbound(arr,i,n,0)
            count_ones = n - cnt_zeroes
            if count_ones > max_ones:
                max_ones = count_ones
                ans = i
        return ans
