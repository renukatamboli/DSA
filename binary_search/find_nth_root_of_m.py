class Solution:
    def getfunc(self,mid,n,m):
        ans = 1
        for i in range(n):
            ans = ans*mid
            if ans > m:
                return 2
        if ans == m:
            return 1
        return 0
	def nthRoot(self, n: int, m: int) -> int:
	    low = 1
	    high = m
	    while low <= high:
	        mid = (low+high) // 2
	        num = self.getfunc(mid,n,m)
	        if num == 1:
	            return mid
	        if num == 0:
	            low = mid+1
	        else:
	            high = mid-1
	    return -1
		# Code here
