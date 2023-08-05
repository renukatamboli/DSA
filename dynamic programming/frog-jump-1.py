//https://www.codingninjas.com/studio/problems/frog-jump_3621012?leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *

from typing import *
import sys

def f(index,stones,dp):
        if index == 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        left = f(index-1,stones,dp) + abs(stones[index] - stones[index-1])
        right = sys.maxsize
        if index > 1:
            right = f(index-2,stones,dp) + abs(stones[index] - stones[index-2])
        dp[index] = min(left,right)
        return dp[index]
  
def frogJump(n: int, heights: List[int]) -> int:
    # Write your code here.
    dp = [-1 for i in range(0,n)]
    return f(n-1,heights,dp)
