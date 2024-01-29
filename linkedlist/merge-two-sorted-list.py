# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        newHead = ListNode()
        current = newHead
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                current.next = p2
                p2 = p2.next
            else:
                current.next = p1
                p1 = p1.next
            current = current.next
            
        if p1 is not None:
            current.next = p1
        if p2 is not None:
            current.next = p2
        
        return newHead.next
                
        
