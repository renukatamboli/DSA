from os import *
from sys import *
from collections import *
from math import *

from typing import List

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp = [[-1 for _ in range(0,c)] for _ in range(0,c)]
    for j1 in range(0,c):
        for j2 in range(0,c):
            if j1 == j2:
                dp[j1][j2] = grid[r-1][j1]
            else:
                dp[j1][j2] = grid[r-1][j1] + grid[r-1][j2]
    for i in range(r-2,-1,-1):
        temp = [[-1 for _ in range(0,c)] for _ in range(0,c)]
        for j1 in range(0,c):
            for j2 in range(0,c):
                maxi = -1e8
                for m in range(-1,2):
                    for n in range(-1,2):
                        value = 0
                        if j1 == j2:
                            value = grid[i][j1]
                        else: 
                            value = grid[i][j1] + grid[i][j2]
                        if j1+m >= 0 and j1+m < c and j2+n >= 0 and j2+n <c:
                            value +=  dp[j1+m][j2+n]
                        else:
                            value += -1e8
                        maxi = max(maxi,value)
                temp[j1][j2] = maxi
        dp = temp[:]
    return dp[0][c-1]                      
