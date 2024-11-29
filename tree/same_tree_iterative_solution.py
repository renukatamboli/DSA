# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = []

        queue.append((p,q))
        while queue:
            p,q = queue.pop()
            if not self.check(p,q):
                return False
            if p:
                queue.append((p.left,q.left))
                queue.append((p.right, q.right))
        return True
            
