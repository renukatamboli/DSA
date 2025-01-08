class Solution:
    def solve(self,prev,k,prices,buy,i):
        if k == 0 or i == len(prices):
            return 0
        take = 0
        not_take = 0
        if buy:
            take = self.solve(i,k,prices,False,i+1)
            not_take = self.solve(prev,k,prices,True,i+1)
        else:
            if prices[prev] < prices[i]:
                take = (prices[i] - prices[prev]) + self.solve(i+1,k-1,prices,True,i+1)
            not_take = self.solve(prev,k,prices,False,i+1)
        return max(take,not_take)
        
        
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.solve(-1,k,prices,True,0)
        
