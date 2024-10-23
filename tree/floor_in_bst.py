class Solution:
    def floor(self, root, x):
        cur = root
        floor = -1
        while cur:
            if cur.data == x:
                floor = cur.data
                return floor
            if cur.data > x:
                cur = cur.left
            else:
                floor = cur.data
                cur = cur.right
        return floor
