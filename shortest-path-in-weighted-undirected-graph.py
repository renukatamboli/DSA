#User function Template for python3
from queue import PriorityQueue
class Solution:
    def shortestPath(self, n, m, edges):
        queue = PriorityQueue()
        adj = [[] for i in range(0,n+1)]
        dist = [1e9 for i in range(0,n+1)]
        parent = [i for i in range(0,n+1)]
        path = []
        for node in edges:
            adj[node[0]].append((node[1],node[2]))
            adj[node[1]].append((node[0],node[2]))
        dist[1] = 0
        queue.put((0,1))
        while(queue.qsize() > 0):
            node = queue.get()
            vertex = node[1]
            weight = node[0]
            for entity in adj[vertex]:
                edgW = entity[1]
                v = entity[0]
                if dist[v] > weight + edgW:
                    dist[v] = weight + edgW
                    queue.put((dist[v],v))
                    parent[v] = vertex
        if dist[n] == 1e9:
            return [-1]
        node = n
        #print("node",node,parent)
        #return []
        while(parent[node]!=node):
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()
        return path
            
            
            
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends
