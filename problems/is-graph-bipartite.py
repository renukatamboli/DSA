class Solution(object):
    def check(self, start, graph, color):
        queue = []
        color[start]=0
        queue.append(start)
        while(len(queue)>0):
            node = queue.pop(0)
            for v in graph[node]:
                if(color[v]==-1):
                    color[v] = 1 - color[node]
                    queue.append(v)
                else:
                    if(color[v] == color[node]):
                        return False
        return True
    def isBipartite(self, graph):
        color = [-1 for i in range(0, len(graph))]
        for i in range(0,len(graph)):
            if color[i]==-1:
                if(self.check(i, graph, color) == False):
                    return False
        return True

        """
        :type graph: List[List[int]]
        :rtype: bool
        """
