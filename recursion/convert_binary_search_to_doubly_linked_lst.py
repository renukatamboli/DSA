"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.first = None
        self.last = None
        
    def helper(self,root):
        if root:
            self.helper(root.left)
            
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            self.last = root
            self.helper(root.right)
            
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.first = None
        self.last = None
        
        self.helper(root)
        
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first
