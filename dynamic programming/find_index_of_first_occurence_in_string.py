class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        for i in range(0,len(haystack)):
            if haystack[i:i+l] == needle:
                return i
        return -1
        
