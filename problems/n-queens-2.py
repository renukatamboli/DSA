from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.queenRow = defaultdict(int)
        self.queenDiagonalLeft = defaultdict(int)
        self.queenDiagonalRight = defaultdict(int)

    def isNotValid(self,row,col,n):
        return self.queenRow[row] or self.queenDiagonalLeft[n-1+col-row] or self.queenDiagonalRight[row+col]

    def solve(self,col, board,ans, n):
        if(col==n):
            newBoard = []
            for i in range(n):
                newBoard.append(''.join(board[i]))
            ans.append(newBoard)
            return

        for row in range(0,n):
            if self.isNotValid(row,col,n)!=1:
                self.queenRow[row] = 1
                self.queenDiagonalLeft[n-1+col-row] = 1
                self.queenDiagonalRight[row+col] = 1
                board[row][col] = "Q"
                self.solve(col+1,board,ans, n)
                board[row][col] = "."
                self.queenRow[row] = 0
                self.queenDiagonalLeft[n-1+col-row] = 0
                self.queenDiagonalRight[row+col] = 0

    def solveNQueens(self, n):
        ans = []
        board = [["." for i in range(0,n)] for i in range(0,n)]
        self.solve(0,board, ans, n)
        return ans
        """
        :type n: int
        :rtype: List[List[str]]
        """
