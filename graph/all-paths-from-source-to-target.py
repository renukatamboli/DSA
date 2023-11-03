def DFS(source,destination,graph,queue,visited,ans,temp):
    if source == destination:
        ans.append(temp[:])
    queue.append(source)
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            temp.append(v)
            DFS(v,destination,graph,queue,visited,ans,temp)
            temp.pop()
            visited[v] = False

class Solution(object):
    def allPathsSourceTarget(self, graph):
        visited = [False for _ in range(0,len(graph))]
        temp = [0]
        ans = []
        queue = []
        DFS(0,len(graph)-1,graph,queue,visited,ans,temp)
        return ans
            
            
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
