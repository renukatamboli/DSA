# https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/?envType=problem-list-v2&envId=heap-priority-queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heappop
class Solution:
    def __init__(self):
        self.heap = []
        self.arr = []

    def createHeap(self, root, target):
        if root:
            heappush(self.heap, (abs(target - root.val), root.val))
            self.createHeap(root.left, target)
            self.createHeap(root.right, target)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ans = []
        if not root:
            return ans
        self.createHeap(root,target)
        while k != 0:
            diff, value = heappop(self.heap)
            ans.append(value)
            k-=1
        return ans

        
