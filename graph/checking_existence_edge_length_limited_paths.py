class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return True
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        return False
    
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        edgeList.sort(key = lambda x: x[2])
        j = 0
        ans = [False]* len(queries)
        queries_with_index = [(x, y, limit, idx) for idx, (x, y, limit) in enumerate(queries)]
        queries_with_index.sort(key=lambda x: x[2])
        for x,y,limit,idx in queries_with_index:
            while j < len(edgeList) and edgeList[j][2] < limit:
                u, v, _  = edgeList[j]
                uf.union(u,v)
                j+=1
            ans[idx] = uf.isConnected(x,y)
        return ans
