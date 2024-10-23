# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        cur = root
        while cur:
            if cur.left is None:
                arr.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                if prev.right == cur:
                    arr.append(cur.val)
                    prev.right = None
                    cur = cur.right
        i = 0
        l = len(arr)
        for query in queries:
            ceil = -1
            floor = -1
            left = 0
            right = l-1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] <= query:
                    floor = arr[mid]
                    left = mid+1
                else:
                    right = mid-1

            left = 0
            right = l-1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] >= query:
                    ceil = arr[mid]
                    right = mid-1
                else:
                    left = mid + 1 
            ans.append([floor,ceil])
        return ans 
        
