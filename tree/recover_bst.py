# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        cur = root
        first = None
        last = None
        ptr = None
        while cur:
            if cur.left is None:
                if ptr and ptr.val > cur.val:
                    if not first:
                        first = ptr
                    last = cur
                ptr = cur
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    if ptr and ptr.val > cur.val:
                        if not first:
                            first = ptr
                        last = cur
                    ptr = cur
                    cur = cur.right
        
        if first and last:
            first.val, last.val = last.val, first.val


        """
        Do not return anything, modify root in-place instead.
        """
        
