from collections import defaultdict
class UnionFind:
    def __init__(self, size):
        self.rank = [0 for _ in range(size)]
        self.root = [i for i in range(size)]
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootX
        else:
            self.rank[rootX] += 1
            self.root[rootY] = rootX
    
    def isConnected(self,x,y):
        return self.find(x) != self.find(y)
        
class Solution:
    def isvalid(self, row, col, m, n, grid):
        return row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m*n)
        adj_row = [0, -1, 0, 1]
        adj_col = [-1, 0, 1, 0]
        for i in range(m):
            for j in range(n):
                node  = i*n + j
                if grid[i][j] == 1:
                    for t in range(4):
                        row = i + adj_row[t]
                        col = j + adj_col[t]
                        if self.isvalid(row, col, m, n, grid):
                            adj_node = row*n + col
                            uf.union(node, adj_node)
        
        islands = defaultdict(list)
        shapes = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    node = i * n + j
                    root = uf.find(node)
                    islands[root].append((i,j))
        
        for island_cells in islands.values():
            min_i = min(x for x, y in island_cells)
            min_j = min(y for x, y in island_cells)
            normalized = sorted((x - min_i, y - min_j) for x, y in island_cells)
            shapes.add(tuple(normalized))
        
        return len(shapes)


        
