# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        
        h = {}
        
        while(p1 is not None):
            
            if p1 not in h:
                h[p1] = p1
            else:
                return p1
            p1 = p1.next
        
        return None
