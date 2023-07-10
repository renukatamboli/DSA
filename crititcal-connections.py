#User function Template for python3

class Solution:
    def __init__(self):
        self.timer = 1
        
    
    def dfs(self,node,parent, visited, adj,tin,low,bridges):
        visited[node] = 1
        tin[node] = low[node] = self.timer
        self.timer+=1
        for it in adj[node]:
            if it == parent:
                continue
            if not visited[it]:
                self.dfs(it, node, visited, adj,tin,low,bridges)
                low[node] = min(low[node],low[it])
                if low[it] > tin[node]:
                    bridges.append(tuple(sorted((it,node))))  
            else:
                low[node] = min(low[node],low[it])
                
    def criticalConnections(self, V, adj):
        visited = [0 for i in range(0,V)]
        tin = [0 for i in range(0,V)]
        low = [0 for i in range(0,V)]
        bridges = []
        self.dfs(0,-1,visited,adj,tin,low,bridges)
        bridges.sort()
        return bridges
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends
