class Solution(object):
    def eventualSafeNodes(self, graph):
        graph_rev = [[] for i in range(0,len(graph))]
        queue = []
        indegree = [0 for i in range(0,len(graph))]
        safe_nodes = []
        for i in range(0, len(graph)):
            for v in graph[i]:
                graph_rev[v].append(i)
                indegree[i] += 1
        for i in range(0, len(graph)):
            if indegree[i] == 0:
                queue.append(i)
        while(len(queue)>0):
            node = queue.pop(0)
            safe_nodes.append(node)
            for v in graph_rev[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        safe_nodes.sort()
        return safe_nodes
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
