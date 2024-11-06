class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = []
        stack2 = []
        for char in s:
            if char == "(":
                stack1.append(char)
                stack2.append(char)
            elif char == ")":
                if len(stack1) > 0:
                    stack1.pop()
                if len(stack2) > 0:
                    stack2.pop()
                else:
                    return False
            else:
                if len(stack1) > 0:
                    stack1.pop()
                stack2.append("(")
            if len(stack1) > 0 and len(stack2) == 0:
                return False
        return len(stack1) == 0
        
