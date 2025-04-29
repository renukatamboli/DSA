class Solution:
    def getPath(self,dr, dc):
        if dr == 0 and dc == -1:
            return "l"
        if dr == -1 and dc == 0:
            return "u"
        if dr == 0 and dc == 1:
            return "r"
        if dr == 1 and dc == 0:
            return "d"

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        dis = [[float('inf')] * n for _ in range(m)]
        paths = [['']*n for _ in range(m)]
        dis[ball[0]][ball[1]] = 0
        
        heap = [(0, '', ball[0], ball[1])]  # (distance, row, col)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            d, path, row, col = heappop(heap)
            print("path", path,"row", row,"col", col)
            if [row, col] == hole:
                return paths[row][col]
            for dr, dc in directions:
                r, c, steps = row, col, 0
                # Roll the ball until it hits a wall
                while 0 <= r + dr < m and 0 <= c + dc < n and maze[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                    steps += 1
                    if [r, c] == hole:
                        break
                if dis[row][col] + steps < dis[r][c] or (dis[row][col] + steps == dis[r][c] and paths[r][c] > paths[row][col] + self.getPath(dr,dc)):
                    paths[r][c] = paths[row][col] + self.getPath(dr,dc)
                    dis[r][c] = dis[row][col] + steps
                    heappush(heap, (dis[r][c],paths[r][c], r, c))
                    
        return "impossible"
        
