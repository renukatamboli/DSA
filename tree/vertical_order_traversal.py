# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import PriorityQueue
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        queue.append((root,0,0))
        res = {}
        ans = []
        while queue:
            size = len(queue)
            tnode = queue.pop(0)
            node = tnode[0]
            v = tnode[1]
            l = tnode[2]
            if v not in res:
                res[v] = {}
            if l not in res.get(v):
                res[v][l] = PriorityQueue()
            res[v][l].put(node.val)
            if node.left:
                queue.append((node.left,v-1,l+1))
            if node.right:
                queue.append((node.right,v+1,l+1))
        vert = list(res.keys())
        vert.sort()
        for key in vert:
            nodes = []
            for level, lvalue in res[key].items():
                while lvalue.qsize() > 0:
                    nodes.append(lvalue.get())
                print("nodes",nodes)
            if len(nodes) > 0:
                ans.append(nodes[:])
        return ans

        
