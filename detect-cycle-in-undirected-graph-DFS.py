from typing import List
class Solution:
    def detect(self, src,visited ,adj, parent) -> bool:
        visited[src]=True
        for v in adj[src]:
            if(not visited[v]):
                if(self.detect(v,visited, adj,src)):
                    return True
            else:
                if parent != v:
                    return True
                    
        
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [False for i in range(0,V)]
	    for i in range(0,V):
	        if(not visited[i]):
	            if(self.detect(i,visited,adj, -1)):
	                return True
	    return False
	    
		#Code here


#{ 
 # Driver Code Starts
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
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
