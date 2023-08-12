from os import *
from sys import *
from collections import *
from math import *

from typing import List

def find(i,j1,j2,r,c,grid,dp):
    if j1 < 0 or j2 < 0 or j1 >= c or j2 >= c:
        return -1e8
    
    if i == r-1:
        if j1==j2:
            return grid[i][j1]
        return grid[i][j1]+grid[i][j2]
    
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]

    maxi = -1e8
    for m in range(-1,2):
        for n in range(-1,2):
            value = 0
            if j1 == j2:
                value = grid[i][j1]
            else:
                value = grid[i][j1] + grid[i][j2]
            value +=  find(i+1,j1+m,j2+n,r,c,grid,dp)
            maxi = max(maxi,value)
    dp[i][j1][j2] = maxi
    return dp[i][j1][j2]

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    dp = [[[-1 for _ in range(0,c)] for _ in range(0,c)]for _ in range(0,r)]
    return find(0,0,c-1,r,c,grid,dp)
