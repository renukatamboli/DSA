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
    def countComponents(self, n, edges):
        uf = unionFind(n)
        for ed in edges:
            i = ed[0]
            j = ed[1]
            if not uf.isConnected(i,j):
                uf.unionByRank(i,j)
        return uf.cnt
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
