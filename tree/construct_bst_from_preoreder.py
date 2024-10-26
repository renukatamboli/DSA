# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0

    def build(self,preorder,min_val, max_val):
        if self.i >= len(preorder) or preorder[self.i] < min_val or preorder[self.i] > max_val:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self.build(preorder,min_val,root.val)
        root.right = self.build(preorder,root.val, max_val)
        return root 

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        min_val = -10000000000000000
        max_val = 100000000000000000  
        return self.build(preorder,min_val,max_val)


        
