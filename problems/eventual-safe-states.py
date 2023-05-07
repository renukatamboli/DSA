class Solution(object):
    def dfs(self,node, adj, visited,pathvis):
        visited[node] = True
        pathvis[node] = True
        
        for v in adj[node]:
            if(not visited[v]):
                if self.dfs(v, adj, visited,pathvis):
                    return True
            elif pathvis[v]:
                    return True
        pathvis[node] = False
        return False

    def eventualSafeNodes(self, graph):
        V = len(graph)
        visited = [False for i in range(0,V)]
        pathvis = [False for i in range(0,V)]
        ans = []
        for i in range(0,V):
            if(not visited[i]):
                self.dfs(i,graph, visited,pathvis)
        for i in range(0,V):
            if not pathvis[i]:
                ans.append(i)
        return ans
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
