class Solution:
    def isvalid(self,row, col, m,n , grid, visited):
        return row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1 and not visited[row][col]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        adj_row = [0,-1,0,1]
        adj_col = [-1,0,1,0]
        visited = [[False for _ in range(n)] for _ in range(m)]
        maxi = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    cnt = 0
                    queue.append((i,j))      
                    while queue: 
                        node = queue.pop()
                        r = node[0]
                        c = node[1]
                        if not visited[r][c]:
                            cnt += 1
                            visited[r][c] = True
                            for t in range(4):
                                row = r + adj_row[t]
                                col = c + adj_col[t]
                                if self.isvalid(row,col, m,n,grid, visited):
                                    queue.append((row, col))
                        maxi = max(maxi,cnt)
        return maxi




        
