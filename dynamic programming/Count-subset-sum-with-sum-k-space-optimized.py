from typing import List

def findWays(arr: List[int], k: int) -> int:
    N = len(arr)
    target = k
    dp = [0 for _ in range(target+1)]
    temp = [0 for _ in range(target+1)]
    temp[0] = 1
    dp[0] = 1
        
    if arr[0] <= target:
        dp[arr[0]] = 1
    
    for i in range(1, N):    
        for j in range(1, target+1):
            take = 0
            if j >= arr[i]:
                take = dp[j - arr[i]]
            notTake = dp[j]
            temp[j] = int((take + notTake) % (1e9+7))
        dp = temp[:]
   
    return dp[target]   
    
