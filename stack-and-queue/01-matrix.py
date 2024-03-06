#https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dis = [[0 for _ in range(n)]  for _ in range(m)]
        queue = []
        visited = [[False for _ in range(n)]  for _ in range(m)]
        arow = [0,-1,0,1]
        acol = [-1,0,1,0]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((0,i,j))
                    visited[i][j] = True
        while queue:
            node = queue.pop(0)
            d = node[0]
            r = node[1]
            c = node[2]
            for t in range(4):
                row = r+arow[t]
                col = c+acol[t]
                if row >= 0 and row< m and col>=0 and col< n and not visited[row][col]:
                    dis[row][col] = d+1
                    visited[row][col] = True
                    queue.append((dis[row][col],row,col))
        return dis
                    
            
                
                
        
