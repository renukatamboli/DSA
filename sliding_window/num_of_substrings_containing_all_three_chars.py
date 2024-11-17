class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashset = {}
        i = 0
        n = len(s)
        cnt = 0
        while i < n:
            hashset[s[i]] = i
            if hashset.get('a') is not None and hashset.get('b') is not None and hashset.get('c') is not None:
                mini = min(hashset['a'], hashset['b'], hashset['c'])
                cnt = cnt + mini + 1              
            i+=1
        return cnt
        
