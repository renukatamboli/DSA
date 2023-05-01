class Solution(object):
    def dfs(self, start, graph, color, col):
        color[start] = col
        for v in graph[start]:
            if color[v] == -1:
                if(self.dfs(v, graph, color, 1-col) == False):
                    return False
            else:
                if color[v] == col:
                    return False
        return True

    def isBipartite(self, graph):
        color = [-1 for i in range(0, len(graph))]
        for i in range(0,len(graph)):
            if color[i]==-1:
                if(self.dfs(i, graph, color, 0) == False):
                    return False
        return True

        """
        :type graph: List[List[int]]
        :rtype: bool
        """
