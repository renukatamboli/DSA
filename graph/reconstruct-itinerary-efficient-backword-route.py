from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def DFS(self,source,result):
        self.graph[source].sort(reverse=True)
        destinationLst = self.graph[source]
        while destinationLst:
            nextDest = destinationLst.pop()
            self.DFS(nextDest,result)
        result.append(source)
                
                
        
    def findItinerary(self, tickets):
        for ticket in tickets:
            u = ticket[0]
            v = ticket[1]
            self.add_edge(u,v)
        result = []
        self.DFS("JFK",result)
        result.reverse()
        return result
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
