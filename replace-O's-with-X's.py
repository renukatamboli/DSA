#User function Template for python3

class Solution:
    def DFS(self, row, col, mat, visited,n,m):
        visited[row][col] = True
        delta_col = [-1,0,1,0]
        delta_row = [0,1,0,-1]
        for i in range(0,4):
            nrow = row+delta_row[i]
            ncol = col+delta_col[i]
            if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and not visited[nrow][ncol] and mat[nrow][ncol]=="O"):
                self.DFS(nrow,ncol, mat, visited,n,m)
        
    def fill(self, n, m, mat):
        visited = [[False for i in range(0,m)] for j in range(0,n)]
        for j in range(0,m):
            if(not visited[0][j] and mat[0][j]=="O"):
                self.DFS(0,j, mat, visited,n,m)
            
            if(not visited[n-1][j] and mat[n-1][j] == "O"):
                self.DFS(n-1,j, mat,visited,n,m)
        
        for i in range(0,n):
            if(not visited[i][0] and mat[i][0]=="O"):
                self.DFS(i,0, mat, visited,n,m)
            
            if(not visited[i][m-1] and mat[i][m-1] == "O"):
                self.DFS(i,m-1, mat,visited,n,m)
                
        for i in range(0,n):
            for j in range(0,m):
                #print("i", i, "j",j,"visited", visited[i][j])
                if(not visited[i][j] and mat[i][j] == "O"):
                    mat[i][j]="X"
        
        return mat
                
                
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
