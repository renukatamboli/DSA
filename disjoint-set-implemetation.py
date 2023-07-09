class Disjoint:
    def __init__(self, n):
        self.rank   = [0 for i in range(0,n+1)]
        self.size   = [1 for i in range(0,n+1)]
        self.parent = [i for i in range(0,n+1)]
    
    def findUltPar(self,node):
        if node < len(self.parent) and node == self.parent[node]:
            return node
        self.parent[node] = self.findUltPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self,u,v):
        ult_u = self.findUltPar(u)
        ult_v = self.findUltPar(v)
        if ult_u == ult_v:
            return
        if self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        elif self.rank[ult_u] > self.rank[ult_v]:
            self.parent[ult_v] = ult_u
        else:
            self.parent[ult_v] = ult_u
            self.rank[ult_u]+=1
            
    def unionBySize(self,u,v):
        ult_u = self.findUltPar(u)
        ult_v = self.findUltPar(v)
        if ult_u == ult_v:
            return
        if self.size[ult_u] < self.size[ult_v]:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]
        else:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]


if __name__ == '__main__':
    ds = Disjoint(7)
    ds.unionBySize(1,2)
    ds.unionBySize(2,3)
    ds.unionBySize(4,5)
    ds.unionBySize(6,7)
    ds.unionBySize(5,6)
    if ds.findUltPar(3) == ds.findUltPar(7):
        print("same")
    else:
        print("not same")
    ds.unionBySize(3,7)
    if ds.findUltPar(3) == ds.findUltPar(7):
        print("same")
