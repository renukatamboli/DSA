class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        topo = []
        queue = []
        adj = [[] for i in range(0,numCourses)]
        indegree = [0 for i in range(0,numCourses)]
        for i in range(0,len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        for i in range(0,numCourses):
            for v in adj[i]:
                indegree[v] += 1
        for i in range(0,numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while len(queue)>0:
            node = queue.pop(0)
            topo.append(node)
            for v in adj[node]:
                indegree[v] -= 1
                if(indegree[v] == 0):
                    queue.append(v)
        if(len(topo) == numCourses):
            return True
        return False
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
