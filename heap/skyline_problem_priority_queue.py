import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0],i])
            edges.append([build[1],i])
        
        edges.sort()
        live = []
        ans = []
        idx = 0

        while idx < len(edges):

            cur_x = edges[idx][0]

            while idx < len(edges) and cur_x == edges[idx][0]:
                b = edges[idx][1]
                if buildings[b][0] == cur_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live,[-height,right])
                
                while live and live[0][1] <= cur_x:
                    heapq.heappop(live)
                idx+=1

            max_height = 0
            if live:
                max_height = -live[0][0]

            if not ans or ans[-1][1] != max_height:
                ans.append([cur_x,max_height])
        return ans
