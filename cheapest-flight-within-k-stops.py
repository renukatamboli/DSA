#User function Template for python3
from typing import List

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj = [[] for _ in range(0,n)]
        queue = []
        dist = [1e9 for _ in range(0,n)]
        for it in flights:
            adj[it[0]].append((it[1],it[2]))
        queue.append((0,(src,0)))
        dist[src] = 0
        while(len(queue)>0):
            it = queue.pop(0)
            stops = it[0]
            node = it[1][0]
            dis = it[1][1]
            if stops > k:
                continue
            for ite in adj[node]:
                adjNode = ite[0]
                edgW = ite[1]
                if dis + edgW < dist[adjNode] and stops < k+1:
                    dist[adjNode] = dis + edgW
                    queue.append((stops+1,(adjNode, dis+edgW)))
                
        if dist[dst] == 1e9:
            return -1
        return dist[dst]
            
        
        
            
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends
