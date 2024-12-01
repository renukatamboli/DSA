from collections import defaultdict
class Solution:
    def box_index(self,i,j):
        return 3*(i//3) + (j // 3)

    def place_number(self,rows, cols,boxes,board,i,j, ch):
        board[i][j] = str(ch)
        bit = 1 << ch
        rows[i] |= bit
        cols[j] |= bit
        boxes[self.box_index(i,j)] |= bit

    def remove_number(self,rows, cols,boxes,board,i,j, ch):
        board[i][j] = "."
        bit = 1 << ch
        rows[i] &= ~bit
        cols[j] &= ~bit
        boxes[self.box_index(i,j)] &= ~bit

    def isValid(self,rows,cols,boxes,row,col,ch):
        bit = 1<<ch 
        return not (bit & rows[row] or bit & cols[col] or bit & boxes[self.box_index(row,col)])

    def solve(self,board,rows,cols,boxes, empty_cells,index):
        if index == len(empty_cells):
            return True
        i,j = empty_cells[index] 
        for ch in range(1,10):
                if self.isValid(rows,cols,boxes,i,j, ch):
                    self.place_number(rows,cols,boxes,board,i,j,ch)
                    if self.solve(board,rows,cols,boxes, empty_cells, index+1):
                        return True
                    self.remove_number(rows,cols,boxes,board,i,j,ch)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    bit = 1 << num
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[self.box_index(i, j)] |= bit
                else:
                    empty_cells.append((i,j))
        self.solve(board,rows,cols,boxes, empty_cells,0)
        
