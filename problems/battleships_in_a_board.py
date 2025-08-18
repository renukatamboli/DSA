class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == "X":
                        continue
                    if j > 0 and board[i][j-1] == "X":
                        continue
                    count+=1
        return count
