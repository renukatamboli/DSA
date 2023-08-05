//https://www.codingninjas.com/studio/problems/frog-jump_3621012?leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *

from typing import *
import sys


  
def frogJump(n: int, heights: List[int]) -> int:
    # Write your code here.
    prev = 0
    prev2 = 0
    for i in range(1,n):
        fs = prev + abs(heights[i]-heights[i-1])
        ss = sys.maxsize
        if i > 1:
            ss = prev2 + abs(heights[i]-heights[i-2])
        curri = min(fs,ss)
        prev2 = prev
        prev= curri
    return prev

