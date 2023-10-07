https://www.codingninjas.com/studio/problems/cost-to-cut-a-chocolate_3208460?leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def find(i,j,cuts,dp):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mini = 1e9
    for k in range(i,j+1):
        cost = (cuts[j+1]-cuts[i-1])+find(i,k-1,cuts,dp)+find(k+1,j,cuts,dp)
        mini = min(cost,mini)
    dp[i][j] = mini%(1e9+7)
    return int(dp[i][j])



def cost(n: int, c: int, cuts: List[int]) -> int:
    dp = [[-1 for _ in range(0,c+2)]for _ in range(0,c+2)]
    cuts.append(n)
    cuts.insert(0,0)
    cuts.sort()
    return find(1,c,cuts,dp)
