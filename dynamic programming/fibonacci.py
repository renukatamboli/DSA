def fibonacci(n,dp):
    if n == 1 or n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibonacci(n-1,dp)+fibonacci(n-2,dp)
    return dp[n]



if __name__ == "__main__":
    dp = [-1 for i in range(0,6)]
    print(fibonacci(5,dp))
