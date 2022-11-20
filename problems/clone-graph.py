"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        queue = []
        queue.append(node)
        cloned_nodes = dict()
        cloned_nodes[node] = Node(node.val)
        while(len(queue) != 0 ):
            source = queue.pop(0)
            source_clone_node = cloned_nodes[source]
            neighbors = source.neighbors
            for i in range(0,len(neighbors)):
                if neighbors[i] not in cloned_nodes:
                    queue.append(neighbors[i])
                    cloned_nodes[neighbors[i]] = Node(neighbors[i].val)
                source_clone_node.neighbors.append(cloned_nodes[neighbors[i]])
        return cloned_nodes[node]
        
        
