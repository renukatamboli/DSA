#User function Template for python3
from queue import PriorityQueue
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        pq = PriorityQueue()
        visited = [0 for i in range(0,V)]
        pq.put((0,0))
        s = 0
        while not pq.empty():
            it = pq.get()
            node = it[1]
            wt = it[0]
            if visited[node]==1:
                continue
            visited[node] = 1
            s+=wt
            for v in adj[node]:
                adjNode = v[0]
                edW = v[1]
                if not visited[adjNode]:
                    pq.put((edW,adjNode))
        return s
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
