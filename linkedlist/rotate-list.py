# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==0 or head.next is None:
            return head
        l = 0
        p = head
        while p is not None:
            p = p.next
            l+=1
        if k%l == 0:
            return head
        if l==k:
            return head
        elif l>k:
            l = l-k
        else:
            r = k//l
            l = l - abs(r*l - k)
        p = head
        prev = p
        while l>0:
            prev = p
            p = p.next
            l-=1
        prev.next = None
        current = p
        while p.next is not None:
            p = p.next
        p.next = head
        head = current
        return head
        
