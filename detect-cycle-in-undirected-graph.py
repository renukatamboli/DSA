from typing import List
class Solution:
    def detect(self, src,visited ,adj) -> bool:
        queue = []
        queue.append((src,-1))
        visited[src] = True
        while(len(queue)>0):
            node = queue.pop(0)
            for v in adj[node[0]]:
                if not visited[v]:
                    queue.append((v,node[0]))
                    visited[v] = True
                else:
                    if(node[1] != v):
                        return True
        return False            
        
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [False for i in range(0,V)]
	    for i in range(0,V):
	        if(not visited[i]):
	            if(self.detect(i,visited,adj)):
	                return True
	    return False
