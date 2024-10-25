

class Solution:
    
    
    def isValidBST(self,root,min_val,max_val):
        if not root:
            return True
        if root.data < min_val or root.data > max_val:
            return False
        return self.isValidBST(root.left, min_val, root.data) and self.isValidBST(root.right, root.data, max_val) 
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        if not root:
            return False
        min_val = -(root.data)
        max_val = root.data
        return self.isValidBST(root, min_val, max_val)
        #code here
