"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return         
        stack = []
        ans = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            if node.children:
                node.children.reverse()
                for child in node.children:
                    stack.append(child)
        return ans    
            
        
