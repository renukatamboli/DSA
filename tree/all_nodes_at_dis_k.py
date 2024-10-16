# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return
        queue = []
        parents = {}
        parents[root] = -1
        dis = 0
        visited = set()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
        queue.append(target)
        while queue:
            size = len(queue)
            if dis == k:
                break
            for _ in range(size):
                node = queue.pop(0)
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                if parents[node] != -1 and parents[node] not in visited:
                    visited.add(parents[node])
                    queue.append(parents[node])
                visited.add(node)
            dis += 1
        ans = []
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
        return ans
        
        
