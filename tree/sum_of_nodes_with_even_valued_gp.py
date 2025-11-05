# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, p, gp):
        if not root:
            return 0
        s = 0
        if gp and gp.val % 2 == 0:
            s += root.val
        s = s + self.solve(root.left, root, p) + self.solve(root.right, root, p)
        return s
    
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, None, None)
