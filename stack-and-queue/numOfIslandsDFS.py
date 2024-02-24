class Solution:
    
    def isValid(self,row,col,m,n,grid,visited):
        return row>=0 and row<m and col>=0 and col<n and grid[row][col] == "1" and not visited[row][col]
    
    def DFS(self,row,col,adj_row,adj_col,m,n,grid,visited):
        visited[row][col] = True
        for i in range(4):
            arow = row+adj_row[i];
            acol = col+adj_col[i];
            if self.isValid(arow,acol,m,n,grid,visited):
                self.DFS(arow,acol,adj_row,adj_col,m,n,grid,visited)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        adj_row = [0,-1,0,1]
        adj_col = [-1,0,1,0]
        islands = 0
        for i in range(0,m):
            for j in range(0,n):
                if self.isValid(i,j,m,n,grid,visited):
                    islands+=1
                    self.DFS(i,j,adj_row,adj_col,m,n,grid,visited)
        return islands
