#User function Template for python3


class Solution:
    def dfsCheck(self,i,adj,vis,pathvis):
        vis[i] = True
        pathvis[i] = True
        
        for v in adj[i]:
            if not vis[v]:
                if self.dfsCheck(v,adj,vis,pathvis):
                    return True
            if pathvis[v]:
                return True
        pathvis[i] = False
        return False
        
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        vis = [False for i in range(0,V)]
        pathvis = [False for i in range(0,V)]
        for i in range(0,V):
            if(self.dfsCheck(i,adj,vis,pathvis)):
                return True
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
