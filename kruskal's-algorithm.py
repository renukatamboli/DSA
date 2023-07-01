#User function Template for python3
class Disjoint:
    def __init__(self, n):
        self.rank   = [0 for i in range(0,n+1)]
        self.size   = [0 for i in range(0,n+1)]
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
        if self.size[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        elif self.rank[ult_u] > self.rank[ult_v]:
            self.parent[ult_v] = ult_u
        else:
            self.parent[ult_v] = ult_u
            self.rank[ult_u]+=1
            
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        edges = []
        for i in range(0,V):
            for it in adj[i]:
                adjNode = it[0]
                wt = it[1]
                node = i
                
                edges.append([wt,node,adjNode])
        totalWt = 0
        edges.sort()
        ds = Disjoint(V)
        for it in edges:
            edgeWt = it[0]
            node = it[1]
            adjNode = it[2]
            
            if ds.findUltPar(node) != ds.findUltPar(adjNode):
                totalWt += edgeWt
                ds.unionByRank(node, adjNode)
        return totalWt
            
                
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
