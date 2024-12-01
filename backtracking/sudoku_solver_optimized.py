from collections import defaultdict
class Solution:
    def box_index(self,i,j):
        return 3*(i//3) + (j // 3)

    def place_number(self,rows, cols,boxes,board,i,j, ch):
        board[i][j] = str(ch)
        rows[i][ch] += 1
        cols[j][ch] += 1
        boxes[self.box_index(i,j)][ch] += 1

    def remove_number(self,rows, cols,boxes,board,i,j, ch):
        board[i][j] = "."
        del rows[i][ch]
        del cols[j][ch]
        del boxes[self.box_index(i,j)][ch]

    def isValid(self,rows,cols,boxes,row,col,ch): 
        return not (ch in rows[row] or ch in cols[col] or ch in boxes[self.box_index(row,col)])

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
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i][num] += 1
                    cols[j][num] += 1
                    boxes[self.box_index(i, j)][num] += 1
                else:
                    empty_cells.append((i,j))
        self.solve(board,rows,cols,boxes, empty_cells,0)
        
