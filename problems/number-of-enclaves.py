class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(0,n)] for j in range(0,m)]
        queue = []
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        cnt = 0
        for i in range(0,m):
            for j in range(0,n):
                if(i==0 or i==m-1 or j==0 or j==n-1):
                    if(grid[i][j]==1):
                        queue.append((i,j))
                        visited[i][j]=1
        while(len(queue)>0):
            node = queue.pop(0)
            row = node[0]
            col = node[1]
            for i in range(0,4):
                nrow = row + delta_row[i]
                ncol = col + delta_col[i]
                if(nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and visited[nrow][ncol] != 1 and grid[nrow][ncol] ==1):
                    queue.append((nrow,ncol))
                    visited[nrow][ncol]=1
        for i in range(0,m):
            for j in range(0,n):
                if(grid[i][j]==1 and visited[i][j] != 1):
                    cnt+=1
        return cnt                    
