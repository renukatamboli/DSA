#User function Template for python3

class Solution:
    
    def dfs(self,visited,i, adj,st):
        visited[i] = 1
        for it in adj[i]:
            if not visited[it]:
                self.dfs(visited,it,adj,st)
        st.append(i)
        
    def dfs3(self,visited,i, adj):
        visited[i] = 1
        for it in adj[i]:
            if not visited[it]:
                self.dfs3(visited,it,adj)
        
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        visited = [0 for i in range(0,V)]
        st = []
        for i in range(0,V):
            if not visited[i]:
                self.dfs(visited, i, adj ,st)
        
        adjT = [[] for i in range(0,V)]
        for i in range(0,V):
            visited[i] = 0
            for it in adj[i]:
                adjT[it].append(i)
        cnt = 0
        while len(st)>0:
            node = st.pop()
            if not visited[node]:
                cnt+=1
                self.dfs3(visited,node,adjT)
                
        return cnt    
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends
