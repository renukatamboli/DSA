from os import *
from sys import *
from collections import *
from math import *

from typing import List

def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    dp = [[0 for _ in range(x+1)] for _ in range(n)]
    for total in range(0,x+1):
        if total%num[0] == 0:
            dp[0][total] = int(total/num[0])
        else:
            dp[0][total] = 1e9
    for ind in range(1,n):
        for total in range(1,x+1):
            notTake = dp[ind-1][total]
            take = 1e9
            if num[ind] <= total:
                take = 1 + dp[ind][total-num[ind]]
            dp[ind][total] = min(take,notTake) 
    ans = dp[n-1][x]
    if ans == 1e9:
        return -1
    return ans
