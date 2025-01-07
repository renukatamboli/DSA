class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ''
        if num < 0:
            num = num*(-1)
            s+="-"
        n = 0
        t = 1
        while num > 0:
            r = num % 7
            n = n+t*r
            t = t*10
            num = num // 7
        s+=str(n)
        return s
            
        
