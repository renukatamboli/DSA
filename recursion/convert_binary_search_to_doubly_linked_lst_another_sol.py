"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def connectList(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        l1_last = l1.left
        l2_last = l2.left
        
        l1_last.right = l2
        l2.left = l1_last
        l2_last.right = l1
        l1.left = l2_last
        
        
        return l1
        
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        leftlist = self.treeToDoublyList(root.left)
        rightlist = self.treeToDoublyList(root.right)
        
        root.left = root
        root.right = root
        
        return self.connectList(self.connectList(leftlist,root),rightlist)
