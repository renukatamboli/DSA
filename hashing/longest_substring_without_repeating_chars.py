class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = {}
        left = 0
        right = 0
        n = len(s)
        l = 0
        while right < n:
            if s[right] in hash_set:
                left = max(hash_set[s[right]]+1,left)
            hash_set[s[right]] = right
            l = max(l,right-left+1)
            right+=1
        return l
