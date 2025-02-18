"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 1
        if not root:
            return 0
        if root.children:
            for child in root.children:
                ans = max(ans,1+self.maxDepth(child))
        return ans
        
