from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for char in s:
            h1[char] += 1
        for char in t:
            h2[char] += 1
        if h1.keys() != h2.keys():
            return False
        for char in h1.keys():
            if h1[char] != h2[char]:
                return False
        return True

        
