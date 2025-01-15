class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = prices[0]
        best = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i] - small > 0:
                best = max(best,prices[i] - small)
            if small > prices[i]:
                small = prices[i]
        return best
            
        
