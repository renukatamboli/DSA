# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        q = head.next
        while p and q:
            if p.val == q.val:
                p.next = q.next
                q = p.next
            else:
                p = q
                q = q.next

        return head
        
