class unionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        
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
            if self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
    
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        total = 0
        uf = unionFind(n+1)
        for i in range(0,n):
            pipes.insert(0,[0,i+1,wells[i]])
        pipes.sort(key=lambda x: x[2])
        for pipe in pipes:
            i = pipe[0]
            j = pipe[1]
            cost = pipe[2]
            if not uf.isConnected(i,j):
                uf.unionByRank(i,j)
                total+=cost
        return total
            
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        
