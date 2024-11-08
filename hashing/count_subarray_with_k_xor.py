from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, m):
        xr = 0
        hashSet = defaultdict(int)
        count = 0
        n = len(arr)
        for i in range(n):
            xr = xr ^ arr[i]
            y = xr ^ m
            if xr == m:
                count+=1
            count+= hashSet[y]
            hashSet[xr] += 1
        return count
