#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
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
    def Solve(self, n, adj):
        ds = Disjoint(n)
        cntExtras = 0
        cntC = 0
        for it in adj:
            u = it[0]
            v = it[1]
            if ds.findUltPar(u) != ds.findUltPar(v):
                ds.unionByRank(u,v)
            else:
                cntExtras+=1
        for i in range(0,n):
            if ds.parent[i] == i:
                cntC+=1
        ans = cntC - 1
        if ans <= cntExtras:
            return ans
        else:
            return -1
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends
