# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = head
        prev = ListNode()
        prev.next = head
        dummy = prev
        while p is not None:
            if p.val == val:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return dummy.next
                
                
                
