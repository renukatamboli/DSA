from queue import PriorityQueue
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        pq = PriorityQueue()
        dist = [1e9 for i in range(0,V)]
        dist[S] = 0
        pq.put((dist[S],S))
        while(pq.qsize()>0):
            node = pq.get()
            d = node[0]
            vertex = node[1]
            for it in adj[vertex]:
                adjVertex = it[0]
                edgeWeight = it[1]
                
                if(d + edgeWeight < dist[adjVertex]):
                    dist[adjVertex] = d + edgeWeight
                    pq.put((dist[adjVertex],adjVertex))
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
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
