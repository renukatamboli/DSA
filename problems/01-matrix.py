class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        visited = [[0 for i in range(0,n)] for j in range(0,m)]
        dist = [[0 for i in range(0,n)] for j in range(0,m)]
        queue = []
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        for i in range(0,m):
            for j in range(0,n):
                if(mat[i][j] == 0):
                    queue.append((i,j,0))
                    visited[i][j]=1
        while(len(queue)>0):
            node = queue.pop(0)
            row = node[0]
            col = node[1]
            dval = node[2]
            dist[row][col] = dval
            for i in range(0,4):
                nrow = delta_row[i]+row
                ncol = delta_col[i]+col
                if(nrow>=0 and nrow < m and ncol>=0 and ncol<n and visited[nrow][ncol] !=1):
                    queue.append((nrow,ncol,dval+1))
                    visited[nrow][ncol]=1
        return dist
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
