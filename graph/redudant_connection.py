class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size+1)]
        self.rank = [1]*(size+1)
    
    def find(self,x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        ans = []
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if not uf.connected(u,v):
                uf.union(u,v)
            else:
                ans.append(edge)
        return ans[-1]
