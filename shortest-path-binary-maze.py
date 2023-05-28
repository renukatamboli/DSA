#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        n = len(grid)
        m = len(grid[0])
        dist = [[1e9 for i in range(0,m)] for j in range(0, n)]
        queue = []
        dist[source[0]][source[1]] = 0
        queue.append((0,source[0],source[1]))
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        while(len(queue)>0):
            node = queue.pop(0)
            dis = node[0]
            row = node[1]
            col = node[2]
            for i in range(0,4):
                newr = row + delta_row[i]
                newc = col + delta_col[i]
                if(newr >= 0 and newr < n and newc >=0 and newc < m and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]):
                    dist[newr][newc] = 1 + dis
                    if newr == destination[0] and newc == destination[1]:
                        return dist[newr][newc]
                    queue.append((1+dis, newr, newc))
        if dist[destination[0]][destination[1]] == 1e9:
            return -1
        return dist[destination[0]][destination[1]]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends
