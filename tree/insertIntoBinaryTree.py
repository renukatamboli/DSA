# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,val):
        if root.val >= val:
            if root.left:
                self.inorder(root.left,val)
            else:
                node = TreeNode(val)
                root.left = node
        else:
            if root.right:
                self.inorder(root.right,val)
            else:
                node = TreeNode(val)
                root.right = node
                
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            root = node
            return root
        self.inorder(root,val)
        return root

        
