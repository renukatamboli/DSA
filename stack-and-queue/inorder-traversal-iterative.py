# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        cur = root
        stack = []
        
        while cur is not None or len(stack)>0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.ans.append(cur.val)
            cur = cur.right
        return self.ans
            
        
