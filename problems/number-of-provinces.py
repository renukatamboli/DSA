from collections import defaultdict
class Solution(object):
    def addEdge(self,u,v, graph):
        graph[u].append(v)

    def DFS(self,visited,queue, graph):
        while(len(queue) > 0):
            #print("queue",queue, graph[queue[0]])
            node = queue.pop()
            for u in graph[node]:
                if(visited[u]!=True):
                    visited[u]=True
                    queue.append(u)
                    self.DFS(visited, queue, graph)
        
    def findCircleNum(self, isConnected):
        visited = [False for i in range(0, len(isConnected))]
        queue = []
        count=0
        graph = defaultdict(list)
        for i in range(0, len(isConnected)):
            for j in range(0, len(isConnected)):
                if(isConnected[i][j]==1 and i!=j):
                    self.addEdge(i,j, graph)
        for i in range(0, len(isConnected)):
            if(visited[i]!=True):
                visited[i]=True
                queue.append(i)
                self.DFS(visited,queue, graph)
                count+=1
        return count
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
