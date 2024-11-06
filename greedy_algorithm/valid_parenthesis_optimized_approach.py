class Solution:
    def checkValidString(self, s: str) -> bool:
        mini = 0
        maxi = 0
        for char in s:
            if char == "(":
                mini += 1
                maxi += 1
            elif char == ")":
                mini -= 1
                maxi -= 1
            else:
                mini -= 1
                maxi += 1
            if maxi < 0:
                return False
            if mini < 0:
                mini = 0
        return mini == 0
        
