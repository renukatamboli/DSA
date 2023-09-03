from os import *
from sys import *
from collections import *
from math import *

def lcs(x,y,s1,s2):
    dp = [0 for i in range(0,y+1)]
    for i in range(1,x+1):
        temp = [0 for i in range(0,y+1)]
        for j in range(1,y+1):
            if s1[i-1] == s2[j-1]:
                temp[j] = 1 + dp[j-1]
            else:
                temp[j] = max(dp[j],temp[j-1])
        dp = temp[:]
    return dp[y]

def longestPalindromeSubsequence(s):
    # Write your code here.
    s1 = s
    s2 = s[::-1]
    return lcs(len(s),len(s),s1,s2)
