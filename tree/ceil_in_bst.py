class Solution:
    def findCeil(self,root, inp):
        ceil = -1
        cur = root
        while cur:
            if cur.key == inp:
                ceil = cur.key
                return ceil
                
            if cur.key > inp:
                ceil = cur.key
                cur = cur.left
            else:
                cur = cur.right
        return ceil
        # code here
