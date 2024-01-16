# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        
        while(p1 is not None and p2 is not None and p2.next is not None):
            p1 = p1.next
            p2 = p2.next.next
            
            if p2 == p1:
                return True
        
        return False
        
