class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = 0
        l = 0
        n = len(s)
        hashset = {}
        maxlen = 0
        maxChars = 0
        while r < n:
            if s[r] not in hashset:
                hashset[s[r]] = 1
            else:
                hashset[s[r]] += 1
            maxChars = max(maxChars,hashset[s[r]])
            while r-l+1 - maxChars > k:
                hashset[s[l]]-=1
                l+=1
            maxlen = max(maxlen,r-l+1)
            r += 1
        return maxlen

