class Solution:
    def minPartition(self, N):
        currency = [1,2,5,10,20,50,100,200,500,2000]
        l = len(currency)
        coins = []
        while N > 0:
            for i in range(l-1,-1,-1):
                if currency[i] <= N:
                    N -= currency[i]
                    coins.append(currency[i])
                    break
        return coins
        # code here
