
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        dp_buy = 0
        dp_sell = 0
        for ind in range(n-1,-1,-1):
            temp_buy = max(dp_buy ,dp_sell-prices[ind])
            temp_sell = max(prices[ind]+dp_buy,dp_sell)
            dp_buy = temp_buy
            dp_sell = temp_sell
        return dp_buy
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
