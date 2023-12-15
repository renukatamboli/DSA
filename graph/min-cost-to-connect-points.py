class Union:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    def find(self,x):
        if x == self.root[x]:
            return x
        x = self.find(self.root[x])
        return x
    
    def unionByRank(self,u,v):
        X = self.find(u)
        Y = self.find(v)
        
        if self.rank[X] > self.rank[Y]:
            self.root[Y] = X
        elif self.rank[X] < self.rank[Y]:
            self.root[X] = Y
        else:
            self.root[Y] = X
            self.rank[X]+=1
    
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = []
        cost = 0
        visited = [False for _ in range(n)]
        for i in range(n-1):
            p1 = points[i]
            x1 = p1[0]
            y1 = p1[1]
            for j in range(i+1,n):
                p2 = points[j]
                x2 = p2[0]
                y2 = p2[1]
                dist = abs(x1-x2)+abs(y1-y2) 
                adj.append((i,j,dist))
        adj.sort(key = lambda x:x[2])
        m = len(adj)
        if m==0:
            return 0
        queue = [adj[0]]
        uf = Union(n)
        for i in range(m):
            p1 = adj[i][0]
            p2 = adj[i][1]
            dist = adj[i][2]
            if not uf.isConnected(p1,p2):
                uf.unionByRank(p1,p2)
                cost+=dist
        return cost
