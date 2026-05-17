#https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        while i < len(s):
            while i >= 0 and i < len(s) and s[i] == "*":
                s = s[:i-1] + s[i+1:]
                i-=2
            i += 1
        return s
