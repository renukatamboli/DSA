class Solution(object):
    def is_safe(self,row, col, board, n):
        duprow=row
        dupcol=col

        while(row>=0 and col>=0):
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1

        row = duprow
        col = dupcol    
        while(col>=0):
            if board[row][col]=="Q":
                return False
            col-=1

        row = duprow
        col = dupcol
        while(row<n and col>=0):
            if board[row][col]=="Q":
                return False
            row+=1
            col-=1

        return True

    def solve(self,col, board,ans, n):
        if(col==n):
            newBoard = []
            for i in range(n):
                newBoard.append(''.join(board[i]))
            ans.append(newBoard)
            return

        for row in range(0,n):
            if(self.is_safe(row, col, board,n)):
                board[row][col] = "Q"
                self.solve(col+1,board,ans, n)
                board[row][col] = "."

    def solveNQueens(self, n):
        ans = []
        board = [["." for i in range(0,n)] for i in range(0,n)]
        self.solve(0,board, ans, n)
        return ans
        """
        :type n: int
        :rtype: List[List[str]]
        """
