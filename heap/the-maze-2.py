from heapq import heappush, heappop
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dis = [[float('inf')] * n for _ in range(m)]
        dis[start[0]][start[1]] = 0
        
        heap = [(0, start[0], start[1])]  # (distance, row, col)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            d, row, col = heappop(heap)
            if [row, col] == destination:
                return d
            for dr, dc in directions:
                r, c, steps = row, col, 0
                # Roll the ball until it hits a wall
                while 0 <= r + dr < m and 0 <= c + dc < n and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                    steps += 1
                if dis[row][col] + steps < dis[r][c]:
                    dis[r][c] = dis[row][col] + steps
                    heappush(heap, (dis[r][c], r, c))
                    
        return -1
