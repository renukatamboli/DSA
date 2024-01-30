"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def __init__(self):
        self.visited = set()
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        while p is not None:
            if p.child is not None:
                lstHead = self.flatten(p.child)
                p.child = None
                temp = p.next
                p.next = lstHead
                lstHead.prev = p
                while lstHead.next is not None:
                    lstHead = lstHead.next
                lstHead.next = temp
                if temp is not None:
                    temp.prev = lstHead
            p = p.next
        return head
