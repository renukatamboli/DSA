class NodeVal:
    
    def __init__(self,min_val,max_val,max_size):
        self.min_val = min_val
        self.max_val = max_val
        self.max_size = max_size
    
class Solution:
    def getLargestBst(self,root):
        max_val = 100000000000000000000
        min_val = -10000000000000000000
        if not root:
            return NodeVal(max_val,min_val,0)
        left = self.getLargestBst(root.left)
        right = self.getLargestBst(root.right)
        
        if left.max_val < root.data < right.min_val:
            return NodeVal(min(left.min_val,root.data),max(right.max_val,root.data),left.max_size+right.max_size+1)
        
        return NodeVal(min_val,max_val, max(left.max_size,right.max_size))
        
    def largestBst(self, root):
        return self.getLargestBst(root).max_size
        # Your code here
