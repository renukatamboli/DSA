#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, row, col, visited, grid, vec, row0, col0,m,n):
        visited[row][col] = 1
        vec.append((row-row0, col - col0))
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        for i in range(0,4):
            nrow = row + delta_row[i]
            ncol = col + delta_col[i]
            if(nrow>=0 and nrow < m and ncol >=0 and ncol < n and grid[nrow][ncol]==1 and not visited[nrow][ncol]):
                self.dfs(nrow,ncol,visited, grid, vec, row0, col0, m,n)
        
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(0,n)] for j in range(0,m)]
        island = set()
        for i in range(0,m):
            for j in range(0,n):
                if not visited[i][j] and grid[i][j] == 1:
                    vec = []
                    self.dfs(i,j, visited, grid, vec, i, j,m,n)
                    island.add(tuple(vec))
        return len(island)
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
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends
