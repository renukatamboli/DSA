"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        queue = [root]
        tree = [[root.val]]
        while len(queue) > 0:
            
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                
                if node.children:
                    for child in node.children:
                        level.append(child.val)
                        queue.append(child)
            if level:
                tree.append(level)
        return tree
                
                
                    
            
