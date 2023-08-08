from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [-1 for i in range(0,4)]
    temp = [-1 for i in range(0,4)]
    dp[0] = max(points[0][1],points[0][2])
    dp[1] = max(points[0][0],points[0][2])
    dp[2] = max(points[0][0],points[0][1])
    dp[3] = max(points[0][0],points[0][1],points[0][2])

    for day in range(1,n):
        for last in range(0,4):
            temp[last] = 0
            for task in range(0,3):
                if task != last:
                    temp[last] = max(points[day][task]+dp[task],temp[last])
        dp = temp[:]
    return dp[3]
