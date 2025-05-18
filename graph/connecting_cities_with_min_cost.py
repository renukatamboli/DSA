from heapq import heappush, heappop
class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size+1)]
        self.rank = [0 for _ in range(size+1)]
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        heap = []
        edge = 0
        uf = UnionFind(n)
        total = 0
        if len(connections) < n-1:
            return -1

        for connection in connections:
            x = connection[0]
            y = connection[1]
            d = connection[2]
            heappush(heap, (d,x,y))
        
        while heap:
            d,x,y = heappop(heap)
            if not uf.isConnected(x,y):
                total += d
                uf.union(x,y)
                edge+=1
            if edge == n-1:
                return total
        return -1
