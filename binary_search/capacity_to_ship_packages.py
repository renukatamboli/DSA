class Solution:
    def calculate(self,weights, cap):
        load = 0
        days = 1
        for wt in weights:
            if load+wt > cap:
                days+=1
                load = wt
            else:
                load+=wt
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        high = 0
        low = max(weights)
        for wt in weights:
            high += wt
        while low <= high:
            mid = (low+high) // 2
            noOfDays = self.calculate(weights,mid)
            if noOfDays <= days:
                high = mid-1
            else:
                low = mid+1
        return low
        
