#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        dist = [int(1e8) for i in range(0,V)]
        dist[S] = 0
        for i in range(0,V):
            for it in edges:
                u = it[0]
                v = it[1]
                wt = it[2]
                if dist[u]!=int(1e8) and wt + dist[u] < dist[v]:
                    dist[v] = wt + dist[u]
        for it in edges:
            u = it[0]
            v = it[1]
            wt = it[2]
            if dist[u]!=int(1e8) and wt + dist[u] < dist[v]:
                return [-1]
        return dist    
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
