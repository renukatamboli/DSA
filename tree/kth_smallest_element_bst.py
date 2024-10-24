# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        inorder = []
        c = 0
        while cur:
            if cur.left is None:
                c+=1
                if c==k:
                    return cur.val
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                if prev.right == cur:
                    prev.right = None
                    c+=1
                    if c==k:
                        return cur.val
                    cur = cur.right
        return -1
                
        
