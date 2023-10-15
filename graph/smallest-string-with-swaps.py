from collections import defaultdict
class unionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.components = {i: [i] for i in range(size)}
    
    def find(self,x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def unionByRank(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.components[rootX].extend(self.components[rootY])
                del self.components[rootY]
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
                self.components[rootY].extend(self.components[rootX])
                del self.components[rootX]
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                self.components[rootX].extend(self.components[rootY])
                del self.components[rootY]
    
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
    
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        slst = list(s)
        uf = unionFind(len(s))
        for ed in pairs:
            i = ed[0]
            j = ed[1]
            if i!=j:
                uf.unionByRank(i,j)
        for root,ele in uf.components.items():
            items = [slst[ele[i]] for i in range(0,len(ele))]
            items.sort()
            ele.sort()
            for i in range(0,len(ele)):
                slst[ele[i]] = items[i]
            
        return "".join(slst)
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
