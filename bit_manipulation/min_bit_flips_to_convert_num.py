class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start ^ goal
        cnt = 0
        for i in range(0,31):
            if num & (1 << i):
                cnt = cnt+1
        return cnt
