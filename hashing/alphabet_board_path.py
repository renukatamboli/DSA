#https://leetcode.com/problems/alphabet-board-path/
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        char_map = {}
        output = ''

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                char_map[ch] = (i, j)
        
        current = (0,0)
        for char in target:
            new = char_map[char]
            diff = new[0] - current[0]
            ch = 'U' if diff < 0 else 'D'
            apndLst = None
            if char == 'z' and current[1] != 0:
                diff -= 1
                apndLst = ch
            for i in range(abs(diff)):
                output += ch
            diff = new[1] - current[1]
            ch = 'R' if diff > 0 else 'L'
            for i in range(abs(diff)):
                output += ch
            if apndLst:
                output += apndLst
            output += "!"
            current = new
        return output
