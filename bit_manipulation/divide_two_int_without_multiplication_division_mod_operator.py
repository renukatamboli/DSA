import sys
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == dividend:
            return 1
        sign = False
        if dividend > 0 and divisor < 0:
            sign = True
        if dividend < 0 and divisor > 0:
            sign = True
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while n >= d:
            cnt = 0
            while n >= (d << cnt+1):
                cnt += 1
            ans += (1 << cnt)
            n -= (d << cnt)
        if ans >= 2**31 and not sign:
            return 2**31-1
        if ans > 2 ** 31 and sign:
            return - 2**31
        if sign:
            return -ans
        return ans    
        
