#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = [[] for i in range(0,n)]
        dist = [10000 for i in range(0,n)]
        queue = []
        for i in range(0,m):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        dist[src] = 0
        queue.append(src)
        while(len(queue)>0):
            node = queue.pop(0)
            for v in adj[node]:
                if dist[node] + 1 < dist[v]:
                    dist[v] = 1+ dist[node]
                    queue.append(v)
        for i in range(0,n):
            if(dist[i] == 10000):
                dist[i] = -1
        return dist
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends
