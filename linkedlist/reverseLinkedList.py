# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        temp = p
        dummy = None
        while p is not None:
            temp = p
            p = p.next    
            temp.next = dummy
            dummy = temp
        return temp
        
