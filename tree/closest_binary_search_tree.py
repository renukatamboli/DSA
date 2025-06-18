# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.closest = -1
        self.diff = 1e9
        
    
    def find(self,root,target):
        if not root:
            return
        diff = abs(target - root.val)
        if self.diff == diff:
            self.closest = min(self.closest, root.val)
        if self.diff > diff:
            self.closest = root.val
            self.diff = diff
        if target <= root.val and root.left:
            self.find(root.left, target)
        else:
            self.find(root.right, target)
            
            
   
        
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.find(root, target)
        return self.closest
        
        
