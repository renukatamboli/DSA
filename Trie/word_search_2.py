from typing import List

class Node:
    def __init__(self):
        self.links = {}
        self.flag = False
    
    def put(self, ch, node):
        self.links[ch] = node
    
    def get(self, ch):
        return self.links.get(ch, None)
    
    def containsKey(self, ch):
        return ch in self.links
    
    def isEnd(self):
        return self.flag

    def setEnd(self):
        self.flag = True

class Solution:
    def __init__(self):
        self.root = Node()
        self.res = []
    
    def insert(self, word: str):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()

    def backtrack(self, row, col, node, word, board, visited, n, m):
        if (
            row < 0 or col < 0 or row >= n or col >= m or 
            visited[row][col] or not node.containsKey(board[row][col])
        ):
            return
        
        visited[row][col] = True
        node = node.get(board[row][col])
        word.append(board[row][col])
        
        if node.isEnd():
            self.res.append("".join(word))
            node.flag = False  # Remove found word to prevent duplicates
        
        # Explore 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.backtrack(row + dr, col + dc, node, word, board, visited, n, m)
        
        visited[row][col] = False
        word.pop()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Insert words into Trie
        for word in words:
            self.insert(word)

        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]

        # Start backtracking from each cell
        for i in range(n):
            for j in range(m):
                self.backtrack(i, j, self.root, [], board, visited, n, m)

        return self.res
