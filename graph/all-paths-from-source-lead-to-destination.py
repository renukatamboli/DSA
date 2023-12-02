class Solution(object):
    def DFS(self,adj,states,source,destination):
        if len(adj[source]) == 0:
            return source == destination
        if states[source] is not None:
            return states[source]
        states[source] = False
        for v in adj[source]:
            if not self.DFS(adj,states,v,destination):
                return False
        states[source] = True
        return True
        
        
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj = [[] for _ in range(n)]
        states = [None for _ in range(n)]
        for ed in edges:
            i = ed[0]
            j = ed[1]
            adj[i].append(j)
        return self.DFS(adj,states,source,destination)
            
        
        
