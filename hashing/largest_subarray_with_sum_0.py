 
class Solution:
    def maxLen(self, arr):
        hashSet = {}
        n = len(arr)
        s = 0
        l = 0
        for i in range(n):
            s = s+arr[i]
            if s == 0:
                l = i+1
            else:
                if s in hashSet:
                    l = max(l,i-hashSet[s])
                else:
                    hashSet[s] = i

            
        return l
        # code here
