from os import *
from sys import *
from collections import *
from math import *

from typing import List
def find(ind,total,notes,dp):
    if ind == 0:
        if total % notes[0] == 0:
            return int(total/notes[0])
        else:
            return 1e9
    if dp[ind][total] != -1:
        return dp[ind][total]
    notTake = find(ind-1,total,notes,dp)
    take = 1e9
    if notes[ind] <= total:
        take = 1 + find(ind,total-notes[ind],notes,dp)
    dp[ind][total] = min(take,notTake)
    return dp[ind][total]

def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    dp = [[-1 for _ in range(x+1)] for _ in range(n)] 
    ans = find(n-1,x,num,dp)
    if ans == 1e9:
        return -1
    return ans
