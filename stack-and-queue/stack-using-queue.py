class MyStack:

    def __init__(self):
        self.queue = []
        self.tail = -1
        self.topEle = -1
        

    def push(self, x: int) -> None:
        self.topEle = x
        self.queue.append(x)
        self.tail+=1
        

    def pop(self) -> int:
        l = len(self.queue)
        while l > 1:
            self.queue.append(self.queue.pop(0))
            l-=1
        node = self.queue.pop(0)
        self.tail-=1
        if self.tail > -1:
            self.topEle = self.queue[self.tail]
        return node
        

    def top(self) -> int:
        return self.topEle
        

    def empty(self) -> bool:
        return self.tail==-1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
