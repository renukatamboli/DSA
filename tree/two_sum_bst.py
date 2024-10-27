# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root, reverse = True):
        self.stack = []
        self.reverse = reverse
        self.pushAll(root)
    
    def pushAll(self,root):
        while root:
            self.stack.append(root)
            if self.reverse:
                root = root.right
            else:
                root = root.left
    
    def next(self):
        top = self.stack.pop()
        if self.reverse:
            self.pushAll(top.left)
        else:
            self.pushAll(top.right)
        return top.val
    
    def hasNext(self):
        return len(self.stack) > 0

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)
        i = l.next()
        j = r.next()
        while i < j:
            if i + j == k:
                return True
            if i + j < k:
                i = l.next()
            else:
                j = r.next()
        return False
        
