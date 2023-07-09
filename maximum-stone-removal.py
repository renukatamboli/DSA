#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
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
            
class Solution:
    def maxRemove(self, adj, n):
        maxRow = 0 
        maxCol = 0
        for it in adj:
            maxRow = max(maxRow, it[0])
            maxCol = max(maxCol, it[1])
        ds = Disjoint(maxRow+maxCol+1)
        for it in adj:
            row = it[0]
            col = it[1]+maxRow+1
            ds.unionBySize(row,col)
        
        cnt = 0
        for it in range(0,maxRow+maxCol+1):
            if ds.parent[it] == it and ds.size[it]>1:
               cnt+=1
        return n - cnt
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        adj = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.maxRemove(adj, n)
        print(res)
# } Driver Code Ends
