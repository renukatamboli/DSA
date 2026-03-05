# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self,node, x):
        if not node:
            return 0
        
        left = self.dfs(node.left, x)
        right = self.dfs(node.right, x)

        if node.val == x:
            self.left = left
            self.right = right
        
        return left + right + 1

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.dfs(root, x)
        if max(n- self.left - self.right - 1, self.left, self.right) > n // 2:
            return True
        return False


        
