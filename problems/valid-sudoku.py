class Solution(object):
    def isValidSudoku(self, board):
        rows = [[0 for x in range(len(board))] for y in range(len(board))] 
        columns = [[0 for x in range(len(board))] for y in range(len(board))]
        grid = [[0 for x in range(len(board))] for y in range(len(board))]
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j] != "."):
                    grid_no = int(i/3)*3+int(j/3)
                    if(rows[i][int(board[i][j])-1]==0):
                        rows[i][int(board[i][j])-1] = 1
                    else:
                        return False
        
        for j in range(0,len(board)):
            for i in range(0,len(board[0])):
                if(board[i][j] != "."):
                    if(columns[j][int(board[i][j])-1]==0):
                        columns[j][int(board[i][j])-1] = 1
                    else:
                        return False
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j] != "."):
                    grid_no = int(i/3)*3+int(j/3)
                    if(grid[grid_no][int(board[i][j])-1]==0):
                        grid[grid_no][int(board[i][j])-1] = 1
                    else:
                        return False          
        return True
