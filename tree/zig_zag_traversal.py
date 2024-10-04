# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = []
        queue.append(root)
        bfs = []
        leftToRight = True
        while queue:
            size = len(queue)
            temp = [0 for _ in range(size)]
            for index in range(size):
                node = queue.pop(0)
                if leftToRight:
                    temp[index] = node.val
                else:
                    temp[size-index-1] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            leftToRight = not leftToRight
            bfs.append(temp[:])
        return bfs
         
