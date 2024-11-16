
class Solution:

    def longestKSubstr(self, s, k):
        hashset = {}
        l = 0
        r = 0
        n = len(s)
        maxlen = -1
        while r < n:
            if s[r] not in hashset:
                hashset[s[r]] = 1
            else:
                hashset[s[r]] += 1
            
            while len(hashset) > k:
                hashset[s[l]] -= 1
                if hashset[s[l]] == 0:
                    del hashset[s[l]]
                l+=1
            if len(hashset) == k:
                maxlen = max(maxlen, r-l+1)
            r+=1
        return maxlen
