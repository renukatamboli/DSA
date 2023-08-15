from os import *
from sys import *
from collections import *
from math import *

from typing import List

def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    dp = [0 for _ in range(x+1)]
    temp = [0 for _ in range(x+1)]
    for total in range(0,x+1):
        if total%num[0] == 0:
            dp[total] = int(total/num[0])
        else:
            dp[total] = 1e9
    for ind in range(1,n):
        for total in range(1,x+1):
            notTake = dp[total]
            take = 1e9
            if num[ind] <= total:
                take = 1 + temp[total-num[ind]]
            temp[total] = min(take,notTake)
        dp = temp[:] 
    ans = dp[x]
    if ans == 1e9:
        return -1
    return ans
