#User function Template for python3
class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_price = -1
            for j in range(i):
                max_price = max(max_price, price[j] + dp[i - j - 1])
            dp[i] = max_price
        return dp[n]
        #dp = [[-1 for _ in range(0,n+1)] for _ in range(0,n)]
        #return self.findSum(n-1, n, price,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
