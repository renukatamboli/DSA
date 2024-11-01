class Solution:
    def solve(self, bt):
        bt.sort()
        wt = 0
        time = 0
        n = len(bt)
        for i in range(n-1):
            time += bt[i]
            wt += time
        return wt // n
