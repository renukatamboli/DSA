class Solution:
    
    def __init__(self):
        self.stack = []
        self.brackets = {"}":"{",")":"(","]":"["}
        self.top = 0
        
        
    def isValid(self, s: str) -> bool:
        self.stack = []
        for i in range(len(s)):
            if s[i] in {"{","[","("}:
                self.stack.append(s[i])
                self.top+=1
            else:
                #print("stack",self.stack[-1],"brackets",self.brackets[s[i]])
                if self.top > 0 and self.stack[-1] == self.brackets[s[i]]:
                        self.stack.pop()
                        self.top-=1
                else:
                    return False
        if self.top == 0:
            return True
        return False
            
        
        
