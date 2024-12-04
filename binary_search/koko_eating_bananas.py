import math
class Solution:
    def getHrs(self,d,piles):
        ans = 0
        for pile in piles:
            ans += math.ceil(pile/d)
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high) // 2
            if self.getHrs(mid,piles) <= h:
                high = mid-1
            else:
                low = mid+1
        return low
