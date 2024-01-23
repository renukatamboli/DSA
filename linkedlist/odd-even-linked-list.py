# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        p1 = head
        p2 = head.next
        temp = p2
        while p1.next is not None and p2.next is not None:
            p1.next = p2.next
            p1 = p2.next
            p2.next = p1.next
            p2 = p1.next
        p1.next = temp
        return head
            
            
