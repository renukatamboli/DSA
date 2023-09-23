#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1
from typing import List


class Solution:
    def find(self,ind,buy,prices,n,dp):
        if ind == n:
            return 0
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        if buy:
            dp[ind][buy] = max(self.find(ind+1,1,prices,n,dp),self.find(ind+1,0,prices,n,dp)-prices[ind])
        else:
            dp[ind][buy] = max(prices[ind]+self.find(ind+1,1,prices,n,dp),self.find(ind+1,0,prices,n,dp))
        return int(dp[ind][buy] % (1e9+7))
    
    
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        dp = [[0 for _ in range(0,2)] for _ in range(0,n+1)]
        return self.find(0,1,prices,n,dp)
        # code here
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends
