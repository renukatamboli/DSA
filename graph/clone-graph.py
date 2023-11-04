"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        self.cloned = {}
        
    def cloneGraph(self, node):
        if node is not None:
            clonedNode = Node(node.val,[])
            self.cloned[node.val] = clonedNode
            for neighbor in node.neighbors:
                if neighbor.val not in self.cloned:
                    neighbor_clone = self.cloneGraph(neighbor)
                    self.cloned[neighbor.val] = neighbor_clone
                else:
                    neighbor_clone = self.cloned[neighbor.val]
                clonedNode.neighbors.append(neighbor_clone)
            return clonedNode
                
            
                
        """
        :type node: Node
        :rtype: Node
        """
        
