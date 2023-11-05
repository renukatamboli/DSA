from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}
        self.ans = []
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def DFS(self,tickets,source,route):
        if len(tickets)+1 == len(route):
            self.ans = route[:]
            return True
        self.graph[source].sort()
        for v in self.graph[source]:
            key = str(source)+"-"+str(v)
            if self.visited[key] > 0:
                self.visited[key] -= 1
                rt = self.DFS(tickets,v,route+[v])
                self.visited[key] += 1
                if rt:
                    return True
                
        route.pop()
        return False
                
                
        
    def findItinerary(self, tickets):
        for ticket in tickets:
            u = ticket[0]
            v = ticket[1]
            self.add_edge(u,v)
            if str(u)+"-"+str(v) in self.visited:
                self.visited[str(u)+"-"+str(v)] += 1
            else:
                self.visited[str(u)+"-"+str(v)] = 1
            #print("visited",self.visited)
        result = ["JFK"]
        self.DFS(tickets,"JFK",result)
        return self.ans
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
