//https://www.codingninjas.com/studio/problems/ninja-s-training_3621003?leftPanelTab=1
from typing import *

def find(day,tno,points,dp):
    if day == 0:
        maxi = 0
        for i in range(0,3):
            if i != tno:
                maxi = max(maxi,points[0][i])
        return maxi
    if dp[day][tno] != -1:
        return dp[day][tno]
    maxi = 0
    for i in range(0,3):
        if i != tno:
            pts = points[day][i] + find(day-1,i,points,dp)
            maxi = max(maxi,pts)
    dp[day][tno] = maxi
    return dp[day][tno]
         
  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for i in range(0,4)] for j in range(0,n)]
    # Write your code here.
    return find(n-1,3,points,dp)
