class Solution:
    def topo_sort(self, edges, n):
        adj = [[] for _ in range(n+1)]
        indegree = [0]*(n+1)
        order = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        queue = []
        for i in range(1,n+1):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            order.append(node)
            n-=1
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        if n!=0:
            return []
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order_rows = self.topo_sort(rowConditions, k)
        order_cols = self.topo_sort(colConditions, k)
        matrix = [[0 for _ in range(1,k+1)] for _ in range(1,k+1)]
        if not order_rows or not order_cols:
            return []
        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_cols[j]:
                    matrix[i][j] = order_rows[i]
        return matrix
