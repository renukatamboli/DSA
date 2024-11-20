class Solution:
    def is_chars_in_hash(self,hashset,poshash):
        for char in hashset.keys():
            if char not in poshash:
                return False
            else:
                if hashset[char] > poshash.get(char):
                    return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        hashset = {}
        poshash = {}
        l = 0
        r = 0
        n = len(s)
        minlen = 100000000000000
        ans = ""
        for char in t:
            if char in hashset:
                hashset[char] += 1
            else:
                hashset[char] = 1
        while r < n:
            if s[r] in poshash:
                poshash[s[r]] += 1
            else:
                poshash[s[r]] = 1
            while self.is_chars_in_hash(hashset,poshash):    
                if minlen > r-l+1:
                    ans = s[l:r+1]
                    minlen = r-l+1
                poshash[s[l]]-= 1
                if poshash[s[l]] == 0:
                    del poshash[s[l]]
                l+=1
            r+=1
        return ans
                
        
