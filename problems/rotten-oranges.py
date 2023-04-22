class Solution(object):
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        queue = []
        visited = [[0 for i in range(0,n)] for j in range(0,m)]
        max_tm = 0
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        cnt_fresh = 0
        for i in range(0,m):
            for j in range(0,n):
                if(grid[i][j] == 2):
                    queue.append((i,j,0))
                    visited[i][j] = 1
                else:
                    visited[i][j] = 0
                if(grid[i][j] == 1):
                    cnt_fresh +=1 
        while(len(queue)>0):
            node = queue.pop(0)
            row = node[0]
            col = node[1]
            tm = node[2]
            max_tm = max(max_tm,tm)
            for i in range(0, 4):
                newRow = row+ delta_row[i]
                newCol = col+ delta_col[i]
                if(newRow>=0 and newRow < m and newCol>=0 and newCol < n and visited[newRow][newCol] != 1 and grid[newRow][newCol] == 1):
                    queue.append((newRow,newCol, tm+1))
                    visited[newRow][newCol] = 1
                    cnt_fresh-=1
        if cnt_fresh != 0:
            return -1
        return max_tm 
