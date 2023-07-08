from typing import List

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
            #print("h1", self.size)
        else:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]
            #print("h2", self.size)
        #print("conver", self.size)

class Solution:
    def isValid(self,newr, newc, n):
        return newr >= 0 and newc >= 0 and newr <n and newc < n
    
    def MaxConnection(self, grid : List[List[int]]) -> int:
        n = len(grid)
        ds = Disjoint(n*n)
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        for row in range(0,n):
            for col in range(0,n):
                if grid[row][col] == 1:
                    for i in range(0, 4):
                        newr = delta_row[i]+row
                        newc = delta_col[i]+col
                        if self.isValid(newr, newc,n) and grid[newr][newc] == 1:
                            adjNode = newr * n + newc
                            node = row * n + col
                            ds.unionBySize(node, adjNode)
        mx = 0
        for row in range(0,n):
            for col in range(0,n):
                components = set()
                if grid[row][col] == 1:
                    continue
                if grid[row][col] == 0:
                    for i in range(0, 4):
                        newr = delta_row[i]+row
                        newc = delta_col[i]+col
                        if self.isValid(newr, newc, n) and grid[newr][newc] == 1:
                            adjNode = newr*n + newc
                            components.add(ds.findUltPar(adjNode))
                sizeTotal = 0
                for it in components:
                    sizeTotal += ds.size[it]
                mx = max(sizeTotal+1,mx)
        
        for cell in range(0,n*n):
            mx = max(mx, ds.size[ds.findUltPar(cell)])
                
        return mx    
        # code here
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.MaxConnection(grid)
        
        print(res)
        

# } Driver Code Ends
