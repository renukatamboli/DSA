#User function Template for python3

from typing import List

class Solution:
    def topoSort(self,node, adj, visited,st):
        visited[node] = True
        for v in adj[node]:
            if not visited[v[0]]:
                self.topoSort(v[0],adj, visited,st)
        st.append(node)
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for i in range(0,n)]
        for i in range(0,m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adj[u].append((v,wt))
            
        visited = [False for i in range(0,n)]
        st = []
        for i in range(0,n):
            if not visited[i]:
                self.topoSort(i,adj,visited,st)
        st.reverse()
        dist = [100000000 for i in range(0,n)]
        dist[0] = 0
        while(len(st)>0):
            node = st.pop(0)
            for u in adj[node]:
                v = u[0]
                wt = u[1]
                if dist[node]+wt < dist[v]:
                    dist[v] = dist[node] + wt
        for i in range(0,n):
            if dist[i] == 100000000:
                dist[i] = -1
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




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



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends
