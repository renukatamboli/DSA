class unionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.cnt = size
    
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def unionByRank(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt -= 1
    
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
    
class Solution(object):
    def earliestAcq(self, logs, n):
        uf = unionFind(n)
        logs.sort()
        for log in logs:
            timestamp = log[0]
            i = log[1]
            j = log[2]
            uf.unionByRank(i,j)
            if uf.cnt == 1:
                return timestamp
        if uf.cnt == 1:
            return logs[n-1][0]
        return -1
        
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        
