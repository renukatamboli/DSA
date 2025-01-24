
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            x = x*(-1)
            flag = 0
        num = 0
        while x != 0:
            r = x % 10
            num = num*10 + r
            x = x // 10
        if num >= (2**31) - 1 or num <= -(2**31):
            return 0
        if flag:
            return num
        return -num

        
