#https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

from collections import defaultdict
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}

        res = []
        end = -1

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        for i, c in enumerate(s):
            if i != first[c]:
                continue

            r = last[c]
            j = i
            valid = True

            while j <= r:
                if first[s[j]] < i:
                    valid = False
                    break
                r = max(r, last[s[j]])
                j += 1
            
            if valid:
                if i > end:
                    res.append("")
                res[-1] = s[i: r+1]
                end = r
        return res
            
            


