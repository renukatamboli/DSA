#User function Template for python3

class Solution:
    def isValid(self,row,col,m,n,visited):
        return row >= 0 and row < n and col >=0 and col < n and visited[row][col] != 1 and m[row][col] == 1
    def getMazePath(self,row,col,m,n,ds,visited,ans):
        adjrow = [-1,0,1,0]
        adjcol = [0,1,0,-1]
        move = ['U','R','D','L']
        if row == n-1 and col == n-1:
            ans.append(''.join(ds[:]))
            return
        
        for i in range(0,4):
            arow = adjrow[i]+row
            acol = adjcol[i]+col
            if self.isValid(arow,acol,m,n,visited):
                ds.append(move[i])
                visited[arow][acol] = 1
                self.getMazePath(arow,acol,m,n,ds,visited,ans)
                visited[arow][acol] = 0
                ds.pop()
    def findPath(self, m, n):
        if m[n-1][n-1] == 0 or m[0][0] == 0:
            return []
        ds = []
        ans = []
        visited = [[0 for i in range(0,n)] for j in range(0,n)]
        visited[0][0] = 1 
        self.getMazePath(0,0,m,n,ds,visited,ans)
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
