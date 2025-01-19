class Solution:
    def isvalid(self,r,c,m,n):
        return r >= 0 and c >= 0 and r < m and c < n
    
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 0
        queue = []
        queue.append((0,0))
        arow = [0,1]
        acol = [1,0]
        while queue:
            node = queue.pop(0)
            row = node[0]
            col = node[1]
            
            if row == m-1 and col == n-1:
                paths+=1
                continue 
                
            for i in range(0,2):
                adj_row = row + arow[i]
                adj_col = col + acol[i]
                if(self.isvalid(adj_row,adj_col,m,n)):
                    queue.append((adj_row,adj_col))
        return paths
        
        
