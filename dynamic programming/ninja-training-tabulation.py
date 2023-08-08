from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for i in range(0,4)] for j in range(0,n)]
    dp[0][0] = max(points[0][1],points[0][2])
    dp[0][1] = max(points[0][0],points[0][2])
    dp[0][2] = max(points[0][0],points[0][1])
    dp[0][3] = max(points[0][0],points[0][1],points[0][2])

    for day in range(1,n):
        for last in range(0,4):
            dp[day][last] = 0
            for task in range(0,3):
                if task != last:
                    dp[day][last] = max(points[day][task]+dp[day-1][task],dp[day][last])

    return dp[n-1][3]
