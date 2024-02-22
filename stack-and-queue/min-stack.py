import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.minValStack = []
        
        

    def push(self, val: int) -> None:
        if len(self.minValStack) == 0 or self.minValStack[-1] >= val:
            self.minValStack.append(val)
            
            
        self.stack.append(val)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minValStack[-1]:
            self.minValStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValStack[-1]

        
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
