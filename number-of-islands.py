#User function Template for python3

from typing import List
class Disjoint:
    def __init__(self, n):
        self.rank   = [0 for i in range(0,n+1)]
        self.size   = [0 for i in range(0,n+1)]
        self.parent = [i for i in range(0,n+1)]
    
    def findUltPar(self,node):
        #print("here", node)
        if node < len(self.parent) and node == self.parent[node]:
            #print("node", node)
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
            
class Solution:
    def isvalid(self,adjr,adjc,n,m):
        return adjr >= 0 and adjr < n and adjc >= 0 and adjc < m
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        n = rows
        m = cols
        ds = Disjoint(n*m)
        visited = [[0 for i in range(0,m)] for j in range(0,n)]
        ans = []
        cnt = 0
        colc = [-1,0,1,0]
        rowr = [0,1,0,-1]
        for cell in operators:
            row = cell[0]
            col = cell[1]
            if visited[row][col] == 1:
                ans.append(cnt)
                continue
            visited[row][col] = 1
            cnt +=1 
            for d in range(0,4):
                adjr = row + rowr[d]
                adjc = col + colc[d]
                if self.isvalid(adjr,adjc,n,m):
                    if visited[adjr][adjc] == 1:
                        adjNode = adjr * m + adjc
                        node = row*m + col
                        if ds.findUltPar(adjNode) != ds.findUltPar(node):
                            cnt-=1
                            ds.unionByRank(node,adjNode)
            ans.append(cnt)
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends
