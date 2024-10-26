class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        successor = None
        
        while root:
            if x.data >= root.data:
                root = root.right
            else:
                successor = root
                root = root.left
        # Code here
        return successor
