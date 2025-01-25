import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        original = s
        s = list(s)
        s.reverse()
        return ''.join(s).lower() == original.lower()
        
