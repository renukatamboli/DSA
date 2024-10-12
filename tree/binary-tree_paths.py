# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPaths(self,root, arr,temp):
        if not root:
            return
        temp.append(str(root.val))
        if not root.left and not root.right:
            arr.append(temp[:])
        self.findPaths(root.left,arr,temp)
        self.findPaths(root.right,arr,temp)
        temp.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if not root:
            return paths
        self.findPaths(root,paths,[])
        paths = ['->'.join(path) for path in paths]
        return paths
        
