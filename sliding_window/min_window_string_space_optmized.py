class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashset = {}
        poshash = {}
        l = 0
        r = 0
        n = len(s)
        m = len(t)
        minlen = 100000000000000
        ans = ""
        cnt = 0
        for char in t:
            if char in hashset:
                hashset[char] += 1
            else:
                hashset[char] = 1
        while r < n:
            if s[r] in hashset:
                if hashset[s[r]] > 0:
                    cnt = cnt+1
                hashset[s[r]] -= 1
            while cnt == m:    
                if minlen > r-l+1:
                    ans = s[l:r+1]
                    minlen = r-l+1
                if s[l] in hashset:
                    hashset[s[l]]+=1
                    if hashset[s[l]] > 0:
                        cnt = cnt-1
                l+=1
            r+=1
        return ans
