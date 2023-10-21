class unionFind:
    
    def __init__(self):
        self.root = {}
        self.rank = {}
    
    def find(self,x):
        if x not in self.root:
            self.root[x] = (x,1)
            self.rank[x] = 1
            
        if self.root[x][0] == x:
            return self.root[x]
        rootX,px = self.find(self.root[x][0])
        self.root[x] = (rootX,self.root[x][1]*px) 
        return self.root[x]
    
    def unionByRank(self,x,y,value):
        rootX, px = self.find(x)
        rootY, py = self.find(y)
        if rootX != rootY:
            multi = px/py*value
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = (rootX, multi)
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = (rootY, 1/multi)
            else:
                self.root[rootY] = (rootX,multi)
                self.rank[rootX] += 1
        
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
    
    def calculate(self,x,y):
        if x not in self.root or y not in self.root:
            return -1.0
        rootX,px = self.find(x)
        rootY,py = self.find(y)
        if rootX != rootY:
            return -1.0
        return 1/px*py
    
class Solution(object):
    def calcEquation(self, equations, values, queries):
        uf = unionFind()
        ans = []
        t = 0
        for k in range(len(equations)):
            eq = equations[k]
            i = eq[0]
            j = eq[1]
            uf.unionByRank(i,j,values[k])
        for query in queries:
            q1 = query[0]
            q2 = query[1]
            value = uf.calculate(q1,q2)
            ans.append(value)
        return ans
            
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
