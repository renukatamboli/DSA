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
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        return True
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def buildMST(self, n, connections, forced=None, skip=None):
        uf = UnionFind(n)
        total = 0
        edges_used = 0

        # Force include an edge if needed
        if forced:
            x, y, w, _ = forced
            if uf.union(x, y):
                total += w
                edges_used += 1

        for x, y, w, idx in connections:
            if idx == skip:
                continue
            if uf.union(x, y):
                total += w
                edges_used += 1
            if edges_used == n - 1:
                break

        return total if edges_used == n - 1 else float('inf')

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [edge + [i] for i, edge in enumerate(edges)]
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])
        weight = self.buildMST(n, edges, None, None)
        critical = []
        pseudo = []
        ans = [] 
        for i in range(len(edges)):
            original_index = edges[i][3]
            new_weight = self.buildMST(n,edges,None,original_index)
            if weight < new_weight:
                critical.append(original_index)
            else:
                new_weight = self.buildMST(n,edges,edges[i],None)
                if weight != -1 and weight == new_weight:
                    pseudo.append(original_index)
        ans.append(critical)
        ans.append(pseudo)
        return ans                
