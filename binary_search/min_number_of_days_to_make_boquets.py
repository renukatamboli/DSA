class Solution:
    def check(self,d, bloomDay, m,k):
        ans = 0
        for day in bloomDay:
            if day <= d:
                ans+=1
            else:
                ans = 0
                
            if ans == k:
                m-=1
                ans = 0
            if m==0:
                break
        return m == 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = min(bloomDay)
        high = max(bloomDay)
        if not self.check(high,bloomDay,m,k):
            return -1
        while low <= high:
            mid = (low+high) // 2
            if self.check(mid,bloomDay,m,k):
                high = mid-1
            else:
                low = mid+1
        return low
