class Solution:
    def getXOR(self,n):
        if n%4 == 0:
            return n
        if n%4 == 1:
            return 1
        if n%4 == 2:
            return n+1
        if n%4 == 3:
            return 0
            
    def findXOR(self, l, r):
        return self.getXOR(r) ^ self.getXOR(l-1)
        # Code here
