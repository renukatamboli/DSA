class Solution(object):

    def isValid(self, row, col, ch, board):
        for i in range(0,9):
            if(board[row][i]==str(ch)):
                return False
            if(board[i][col]==str(ch)):
                return False
            if(board[3*int((row)/3)+int(i/3)][3*int((col)/3)+(i%3)])==str(ch):
                return False
        return True

    def solve(self,board):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if(board[i][j]=="."):
                    for ch in range(1,10):
                        if(self.isValid(i,j,ch,board)):
                            board[i][j] = str(ch)
                            if(self.solve(board)):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True


    def solveSudoku(self, board):
        self.solve(board)
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
